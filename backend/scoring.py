def generate_score_breakdown(features):
    breakdown = {}

    if features.get("has_fee"):
        breakdown["Registration Fee"] = 30

    if features.get("email_type") == "Free Provider":
        breakdown["Free Email Provider"] = 20

    if features.get("salary_risk") != "Normal":
        breakdown["High Salary Claim"] = 15

    return breakdown