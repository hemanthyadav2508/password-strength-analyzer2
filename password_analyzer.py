import re
import string
import secrets


def check_password_strength(password):
    score = 0
    suggestions = []

    # Check length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters (12+ is better).")

    # Check lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    # Check uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    # Check numbers
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add numbers.")

    # Check special characters
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        suggestions.append("Add special characters such as !, @, #, $.")

    # Check repeated characters
    if re.search(r"(.)\1\1", password):
        score -= 1
        suggestions.append("Avoid repeating the same character multiple times.")

    # Common weak passwords
    common_passwords = [
        "password",
        "123456",
        "12345678",
        "qwerty",
        "admin",
        "password123",
        "welcome"
    ]

    if password.lower() in common_passwords:
        score = 0
        suggestions.append("Avoid common passwords.")

    # Determine strength
    if score <= 2:
        strength = "WEAK"
    elif score <= 4:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    return strength, suggestions


def generate_strong_password(length=16):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"

    while True:
        password = ''.join(secrets.choice(characters) for _ in range(length))

        if (
            re.search(r"[a-z]", password)
            and re.search(r"[A-Z]", password)
            and re.search(r"\d", password)
            and re.search(r"[^A-Za-z0-9]", password)
        ):
            return password


# Main program
print("=" * 45)
print("       PASSWORD STRENGTH ANALYZER")
print("=" * 45)

password = input("Enter your password: ")

strength, suggestions = check_password_strength(password)

print("\nPassword Strength:", strength)

if suggestions:
    print("\nSuggestions:")
    for suggestion in suggestions:
        print("-", suggestion)
else:
    print("Your password meets all the basic checks!")

# Generate stronger password
print("\nSuggested Strong Password:")
print(generate_strong_password())

print("\nNote: Do not share your real passwords with anyone.")