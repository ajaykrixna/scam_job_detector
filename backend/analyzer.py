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
You are an expert AI job scam detection system.
Your goal is to determine whether a job posting is:
- Legitimate
- Legitimate but Low-Quality Opportunity
- Suspicious
- Likely Scam
Evaluate the entire job posting using all available evidence.

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

    except Exception as e:
        import traceback

        print("\n===== GEMINI ERROR =====")
        traceback.print_exc()
        print("========================\n")

        return {
            "scam_score": rule_data["rule_score"],
            "verdict": "Rule-Based Analysis Only",
            "red_flags": rule_data["matched_flags"],
            "green_flags": [],
            "recommendation": "AI service temporarily unavailable. Please try again later.",
            "reasoning": "The AI analysis service is currently unavailable due to API limits. Please try again later.",
            "score_breakdown": score_breakdown
        }