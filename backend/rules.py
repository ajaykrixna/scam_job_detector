def rule_based_analysis(content, domain_age):
    content = content.lower()

    score = 0
    red_flags = []

    rules = {
    "registration fee": 40,
    "processing fee": 40,
    "joining fee": 40,
    "security deposit": 40,
    "training fee": 40,
    "application fee": 40,
    "document verification fee": 40,
    "refundable fee": 40,
    "work from home": 5,
    "no experience required": 10,
    "instant joining": 15,
    "limited vacancies": 10,
    "whatsapp": 15,
    "telegram": 15,
    "urgent hiring": 10,
    "immediate joining": 10
}

    for keyword, points in rules.items():
        if keyword in content:
            score += points
            red_flags.append(keyword)

    if "@gmail.com" in content:
        score += 20
        red_flags.append("generic gmail contact")

    if "@yahoo.com" in content:
        score += 20
        red_flags.append("generic yahoo contact")

    if domain_age is not None:
        if domain_age < 30:
            score += 25
            red_flags.append("very new domain")
        elif domain_age < 180:
            score += 10
            red_flags.append("fairly new domain")

    score = min(score, 100)

    return {
        "rule_score": score,
        "matched_flags": red_flags
    }