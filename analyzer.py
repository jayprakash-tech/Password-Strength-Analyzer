import re

def check_password_strength(password):
    strength = 0
    remarks = []
    
    # Check total character length
    if len(password) >= 8:
        strength += 1
    else:
        remarks.append("Password should be at least 8 characters long.")
        
    # Check for number inclusions
    if re.search(r"\d", password):
        strength += 1
    else:
        remarks.append("Add at least one number (0-9).")
        
    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks.append("Add at least one uppercase letter (A-Z).")
        
    # Check for special characters
    if re.search(r"[ !@#$%^&*()_+\-=\[\]{};':\",.<>/?]", password):
        strength += 1
    else:
        remarks.append("Add at least one special character (e.g., @, #, $).")

    # Determine Rating Status
    modes = {1: "Very Weak", 2: "Weak", 3: "Medium", 4: "Strong"}
    rating = modes.get(strength, "Very Weak")
    
    print(f"\nPassword Rating: {rating}")
    if remarks:
        print("Suggestions to improve:")
        for tip in remarks:
            print(f"- {tip}")

# Execute script simulation
user_pass = input("Enter a password to test: ")
check_password_strength(user_pass)
