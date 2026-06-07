import os
import google.generativeai as genai
from dotenv import load_dotenv
import json

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def analyze_job(content, domain_age):
    prompt = f"""
You are a job scam detector.

Domain Age: {domain_age} days

Job Content:
{content[:2000]}

Return ONLY valid JSON in this format:

{{
  "scam_score": 0,
  "verdict": "",
  "reason": ""
}}
"""

    response = model.generate_content(prompt)

    text = response.text.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "").replace("```", "").strip()

    return json.loads(text)