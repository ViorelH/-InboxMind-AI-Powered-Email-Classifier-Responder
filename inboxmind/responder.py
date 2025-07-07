import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_reply(content):
    prompt = f"""Generate a polite, professional reply to the following email:

"{content}"

Keep it brief and human-like.
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content'].strip()
