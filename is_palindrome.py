import re

def is_palindrome(text):
    if not isinstance(text, str):
        return False
    
    # Constraint: Strip non-alphanumeric characters and lowercase
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
    return cleaned == cleaned[::-1]
