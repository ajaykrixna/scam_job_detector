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

Domain Age: {domain_age if domain_age is not None else "Not Available"}

Job Content:
{content[:2000]}

Return ONLY valid JSON in this format:

{{
  "scam_score": 0,
  "verdict": "",
  "red_flags": [],
  "green_flags": [],
  "recommendation": "",
  "reasoning": ""
}}
"""

    try:
        response = model.generate_content(prompt)

        text = response.text.strip()

        if text.startswith("```json"):
            text = text.replace("```json", "").replace("```", "").strip()

        return json.loads(text)

    except Exception:
        return {
            "scam_score": 0,
            "verdict": "Service Error",
            "red_flags": [],
            "green_flags": [],
            "recommendation": "AI service temporarily unavailable. Please try again later.",
            "reasoning": "The AI analysis service is currently unavailable due to API limits. Please try again later."
        }