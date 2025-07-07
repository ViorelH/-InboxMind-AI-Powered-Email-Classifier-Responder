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


