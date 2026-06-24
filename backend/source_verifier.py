from urllib.parse import urlparse

def extract_source_info(url, features):

    source_domain = None

    if url:
        parsed = urlparse(url)

        if parsed.netloc:
            source_domain = parsed.netloc.lower().replace("www.", "")

    email_domain = features.get("email_domain")
    email_type = features.get("email_type")

    observations = []

    if source_domain:
        observations.append("Source domain available")

    if email_type == "Corporate":
        observations.append("Corporate email detected")

    elif email_type == "Free Provider":
        observations.append("Free email provider detected")

    if not source_domain and not email_domain:
        observations.append("No source information available")

    return {
        "source_domain": source_domain,
        "email_domain": email_domain,
        "email_type": email_type,
        "observations": observations
    }