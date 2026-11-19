# Coding exercise only: these are example rules, not verified programme criteria.
# Do not use this function to make real learnership selection decisions.
def check_learnership_eligibility(gender, age, is_employed):
    if gender.lower() != "female":
        return "Ineligible: Program is exclusively for women."
    elif age < 18 or age > 35:
        return "Ineligible: Age must be between 18 and 35."
    elif is_employed:
        return "Ineligible: Must be currently unemployed."
    else:
        return "Eligible! Proceed to technical assessment."
