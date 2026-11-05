import re

def analyze(password):
    score = 0
    tips = []

    if len(password) >= 12:
        score += 25
    else:
        tips.append("Use at least 12 characters.")

    if re.search(r"[A-Z]", password):
        score += 20
    else:
        tips.append("Add uppercase letters.")

    if re.search(r"[a-z]", password):
        score += 20
    else:
        tips.append("Add lowercase letters.")

    if re.search(r"\d", password):
        score += 20
    else:
        tips.append("Add numbers.")

    if re.search(r"[!@#$%^&*()_+=<>?/{}~|-]", password):
        score += 15
    else:
        tips.append("Add special characters.")

    return score, tips


def estimate(score):
    if score < 30:
        return "Very easy to guess"
    elif score < 50:
        return "Could be cracked quickly"
    elif score < 75:
        return "Reasonably strong"
    elif score < 90:
        return "Very strong"
    else:
        return "Excellent"