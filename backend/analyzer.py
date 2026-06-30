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

Important rules:

1. Do NOT classify a job as a scam unless there is concrete evidence such as:
- Registration or application fees
- Advance payment requests
- Identity theft attempts
- Requests for banking or financial information
- Fake recruiter impersonation
- Fake company information
- Impossible salary promises
- Guaranteed income claims
- Pressure tactics to send money

2. Direct sales, field marketing, MLM-style companies, management trainee programs, or aggressive recruitment are NOT automatically scams.
   A direct sales, MLM, or field marketing company may be a poor career choice, but it is not necessarily a scam. Distinguish between a misleading opportunity and fraudulent activity. 

3. Do NOT treat the following alone as evidence of a scam:
- Young domain age
- Missing recruiter email
- Unknown company
- Generic company name
- Generic job description
- Remote work
- Multiple openings
- Performance-based pay
- Unpaid internship
- Google Forms application
- Zoom interviews

Do not treat an unpaid internship, low stipend, or performance-based stipend as a scam indicator by itself.

4. If the application uses Google Forms or another third-party form, mention it as a caution rather than automatically considering it fraudulent.

5. Distinguish between:
- Scam
- Misleading opportunity
- Low-quality job
- Legitimate opportunity

6. Base your final scam score on the strongest evidence, not the number of minor observations.

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

Keep recommendations balanced and professional.
Only recommend avoiding the opportunity when there is strong evidence of fraud.
Otherwise recommend verifying the company, reviewing employee feedback, and asking clarifying questions during the interview.

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