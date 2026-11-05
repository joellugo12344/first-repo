import secrets
import string

def generate(length=16):
    chars = (
        string.ascii_letters
        + string.digits
        + "!@#$%^&*()"
    )

    return "".join(secrets.choice(chars) for _ in range(length))