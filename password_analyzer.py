import re

def check_password_strength(password):
    score = 0
    suggestions = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    # Check lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter (a-z).")

    # Check uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter (A-Z).")

    # Check digits
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add at least one number (0-9).")

    # Check special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Add at least one special character (!@#$...).")

    ratings = {
        1: "Very Weak",
        2: "Weak",
        3: "Medium",
        4: "Good",
        5: "Strong"
    }

    rating = ratings.get(score, "Very Weak")

    print("\n" + "-" * 50)
    print(f"Password entered: {password}")
    print(f"Strength score: {score}/5")
    print(f"Password rating: {rating}")
    print("-" * 50)

    if suggestions:
        print("Suggestions to improve:")
        for tip in suggestions:
            print(f"- {tip}")
    else:
        print("This password meets all basic strength checks.")

password = input("Enter a password to test: ")
check_password_strength(password)
