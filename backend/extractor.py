import re

def detect_salary_risk(content):
    content_lower = content.lower()

    high_salary_terms = [
        "50000",
        "50,000",
        "80000",
        "80,000",
        "100000",
        "1 lakh"
    ]

    no_experience_terms = [
        "no experience",
        "freshers can apply",
        "fresher",
        "students can apply"
    ]

    has_high_salary = any(term in content_lower for term in high_salary_terms)
    has_no_experience = any(term in content_lower for term in no_experience_terms)

    if has_high_salary and has_no_experience:
        return "High"

    return "Normal"

def extract_features(content):
    features = {}

    # Emails
    emails = re.findall(
        r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',
        content
    )

    # Phone numbers
    phones = re.findall(
        r'(?:\+91[- ]?)?[6-9]\d{9}',
        content
    )

    # Salary amounts
    salaries = re.findall(
        r'₹\s?[\d,]+',
        content
    )

    features["emails"] = emails

    free_providers = [
        "gmail.com",
        "yahoo.com",
        "outlook.com",
        "hotmail.com"
    ]

    email_domain = None
    email_type = "Unknown"

    if emails:
        email_domain = emails[0].split("@")[-1].lower()

        if email_domain in free_providers:
            email_type = "Free Provider"
        else:
            email_type = "Corporate"

    features["email_domain"] = email_domain
    features["email_type"] = email_type

    features["phones"] = phones
    features["salaries"] = salaries


    features["has_fee"] = (
    "registration fee" in content.lower()
    or "processing fee" in content.lower()
    or "joining fee" in content.lower()
    )

    features["uses_free_email"] = (
        "@gmail.com" in content.lower()
        or "@yahoo.com" in content.lower()
    )

    features["salary_risk"] = detect_salary_risk(content)

    return features