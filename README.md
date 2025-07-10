# -InboxMind-AI-Powered-Email-Classifier-Responder

# InboxMind 

InboxMind is an AI-powered utility that fetches, classifies, and drafts replies to your emails using GPT-4.

## Features

- Connects to IMAP (e.g. Gmail)
- Classifies emails using GPT-4
- Generates polite responses
- Export-ready for future CSV/JSON

## Setup

git clone https://github.com/ViorelH/inboxmind.git
cd inboxmind
pip install -r requirements.txt
cp .env.template .env
# Fill in your .env with email + OpenAI key

Usage

python examples/run_on_demo_emails.py

License
MIT License


---

###  `setup.py`
```python
from setuptools import setup, find_packages

setup(
    name="inboxmind",
    version="0.1",
    packages=find_packages(),
    install_requires=["openai", "python-dotenv", "pandas"],
    author="Your Name",
    description="AI-powered email classifier and responder",
    keywords=["email", "openai", "automation", "AI"]
)



