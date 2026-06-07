import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def analyze_job(content, domain_age):
    prompt = f"""
    Analyze this job posting.

    Domain age: {domain_age} days

    Job Content:
    {content[:2000]}

    Give a scam risk score from 0 to 100 and explain why.
    """

    response = model.generate_content(prompt)

    return response.text