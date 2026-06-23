import os
import google.generativeai as genai
from dotenv import load_dotenv
import json
from scoring import generate_score_breakdown

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def analyze_job(content, domain_age, rule_data, features):

    score_breakdown = generate_score_breakdown(features)

    prompt = f"""
You are a job scam detector.

Rule Score: {rule_data['rule_score']}

Matched Red Flags:
{rule_data['matched_flags']}

Domain Age:
{domain_age if domain_age is not None else "Not Available"}

Extracted Features:

Emails:
{features["emails"]}

Phone Numbers:
{features["phones"]}

Salary Claims:
{features["salaries"]}

Has Registration Fee:
{features["has_fee"]}

Uses Free Email:
{features["uses_free_email"]}

Salary Risk:
{features["salary_risk"]}

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

        result = json.loads(text)

        result["score_breakdown"] = score_breakdown

        return result

    except Exception:
        return {
            "scam_score": 0,
            "verdict": "Service Error",
            "red_flags": [],
            "green_flags": [],
            "recommendation": "AI service temporarily unavailable. Please try again later.",
            "reasoning": "The AI analysis service is currently unavailable due to API limits. Please try again later.",
            "score_breakdown": score_breakdown
        }