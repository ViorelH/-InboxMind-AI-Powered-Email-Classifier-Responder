import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def classify_email(content):
    prompt = f"""
Classify the following email into one of these categories: 
[Job Offer, Personal, Complaint, Inquiry, Spam, Newsletter, Meeting Request].

Email:
{content}

Return only the category name.
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content'].strip()
