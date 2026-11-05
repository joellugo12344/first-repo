import re

def check_password(password):
    score = 0
    feedback = []

    # Length
    if len(password) >= 12:
        score += 1
    else:
        feedback.append("Use at least 12 characters.")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add an uppercase letter.")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add a lowercase letter.")

    # Number
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add a number.")

    # Symbol
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add a special character.")

    return score, feedback