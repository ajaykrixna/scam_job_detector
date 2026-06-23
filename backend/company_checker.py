import re

KNOWN_COMPANIES = [
    "microsoft",
    "google",
    "amazon",
    "infosys",
    "tcs",
    "wipro",
    "accenture",
    "ibm"
]

def extract_company_name(content):
    content_lower = content.lower()

    for company in KNOWN_COMPANIES:
        if company in content_lower:
            return company

    return None

def check_company_domain(company, source_domain):
    if not company or not source_domain:
        return None

    source_domain = source_domain.lower()

    if company in source_domain:
        return {
            "status": "Match",
            "message": f"Domain appears related to {company.title()}"
        }

    return {
        "status": "Mismatch",
        "message": f"Posting claims to be from {company.title()} but domain does not appear related"
    }

