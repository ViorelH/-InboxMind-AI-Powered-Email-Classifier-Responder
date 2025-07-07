import imaplib
import email
from email.header import decode_header
import os

def fetch_emails(username, password, imap_server="imap.gmail.com", max_emails=5):
    try:
        mail = imaplib.IMAP4_SSL(imap_server)
        mail.login(username, password)
        mail.select("inbox")

        result, data = mail.search(None, "ALL")
        email_ids = data[0].split()[-max_emails:]
        emails = []

        for e_id in email_ids:
            _, msg_data = mail.fetch(e_id, "(RFC822)")
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    subject, encoding = decode_header(msg["Subject"])[0]
                    if isinstance(subject, bytes):
                        subject = subject.decode(encoding or "utf-8")
                    from_ = msg.get("From")
                    body = ""
                    if msg.is_multipart():
                        for part in msg.walk():
                            if part.get_content_type() == "text/plain":
                                body = part.get_payload(decode=True).decode()
                                break
                    else:
                        body = msg.get_payload(decode=True).decode()
                    emails.append({
                        "subject": subject,
                        "from": from_,
                        "body": body
                    })
        return emails
    except Exception as e:
        print(f"Error fetching emails: {e}")
        return []
