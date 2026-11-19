# Practice exercise only: criteria and the named partnership are unverified examples.
# Do not use this code to make real eligibility or enrolment decisions.
def check_kzn_bootcamp_eligibility(gender, province, age):
    if gender.lower() != "female":
        return "Ineligible: Workshop is dedicated to girls and women in tech."
    elif province.upper() not in ["KZN", "KWAZULU-NATAL"]:
        return "Ineligible: Priority is for KwaZulu-Natal residents."
    elif age < 16:
        return "Ineligible: Minimum age requirement is 16."
    else:
        return "Eligible! Welcome to the Connie sons & GirlCode bootcamp."
