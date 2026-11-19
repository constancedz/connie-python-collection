# Coding exercise only: a single mark cannot determine an official matric pass.
# Do not use this function to make real qualification decisions.
def get_matric_pass(mark):
    if mark < 0 or mark > 100:
        return "Invalid mark: Must be between 0 and 100."
    
    if mark >= 80:
        return "Distinction (Bachelor's Pass)"
    elif mark >= 50:
        return "Bachelor's / Diploma Pass"
    elif mark >= 30:
        return "Higher Certificate Pass"
    else:
        return "Not Achieved"
