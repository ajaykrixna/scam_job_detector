import os
import google.generativeai as genai
from dotenv import load_dotenv
import json

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def analyze_job(
    content,
    domain_age,
    rule_data,
    features,
    validation
):
    prompt = f"""
You are a job scam detector.

Company validation is optional.

If no URL is provided and company validation cannot be performed,
 do not treat that as a red flag and do not increase the scam score.
 Only consider company validation suspicious when Domain Match is False.

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

Company Validation:

Detected Company:
{validation["company"]}

Domain Match:
{validation["domain_match"]}

Expected Domain:
{validation.get("expected_domain")}

Actual Domain:
{validation.get("actual_domain")}


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