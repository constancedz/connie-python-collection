# Coding exercise only: length and a number alone do not guarantee a strong password.
# Do not publish or test with real passwords.
def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."
    
    has_number = any(char.isdigit() for char in password)
    if not has_number:
        return "Weak: Password must include at least one number."
    
    return "Strong password!"
