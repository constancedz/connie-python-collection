# Practice format check only: this does not verify a real student ID.
# isdigit() accepts some non-ASCII digits; never publish real student codes.
def validate_student_code(code):
    if not isinstance(code, str) or len(code) != 7:
        return False
    
    if code.startswith("CS-") and code[3:].isdigit():
        return True
    return False
