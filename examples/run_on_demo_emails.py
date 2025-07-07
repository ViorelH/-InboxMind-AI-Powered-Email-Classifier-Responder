from inboxmind.fetcher import fetch_emails
from inboxmind.classifier import classify_email
from inboxmind.responder import generate_reply
import os

# Load credentials from environment
EMAIL = os.getenv("EMAIL_ADDRESS")
PASSWORD = os.getenv("EMAIL_PASSWORD")

emails = fetch_emails(EMAIL, PASSWORD)

for email_data in emails:
    print("Subject:", email_data["subject"])
    print("From:", email_data["from"])
    print("Category:", classify_email(email_data["body"]))
    print("Suggested Reply:\n", generate_reply(email_data["body"]))
    print("="*80)
