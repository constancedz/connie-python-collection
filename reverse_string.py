def reverse_string(text):
    # Constraint: Ensure input is a string
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    
    return text[::-1]
