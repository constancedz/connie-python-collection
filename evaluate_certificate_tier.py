# Coding exercise: these thresholds are examples, not verified certificate criteria.
# Do not use them to make real educational or certification decisions.
def evaluate_certificate_tier(student_name, score):
    if not (0 <= score <= 100):
        return "Invalid score: Must be between 0 and 100."
    
    if score >= 85:
        return f"{student_name}: Certificate of Excellence (Distinction)"
    elif score >= 60:
        return f"{student_name}: Certificate of Achievement (Pass)"
    else:
        return f"{student_name}: Certificate of Participation (Retake Eligible)"
