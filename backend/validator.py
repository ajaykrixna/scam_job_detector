from urllib.parse import urlparse

KNOWN_COMPANIES = {
    "google": "google.com",
    "microsoft": "microsoft.com",
    "amazon": "amazon.jobs",
    "meta": "meta.com",
    "apple": "apple.com",
    "netflix": "netflix.com"
}

def validate_company_domain(content, url):
    if not url:
        return {
            "company": None,
            "domain_match": None
        }

    content_lower = content.lower()

    detected_company = None

    for company in KNOWN_COMPANIES:
        if company in content_lower:
            detected_company = company
            break

    if not detected_company:
        return {
            "company": None,
            "domain_match": "Not Checked"
        }

    domain = urlparse(url).netloc.lower()

    expected_domain = KNOWN_COMPANIES[detected_company]

    return {
        "company": detected_company,
        "domain_match": expected_domain in domain,
        "expected_domain": expected_domain,
        "actual_domain": domain
    }