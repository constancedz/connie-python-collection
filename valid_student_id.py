# Practice format check only: this does not verify a real student ID.
# isdigit() accepts some non-ASCII digits; do not publish real student IDs.
def valid_student_id(student_id):
    return (
        isinstance(student_id, str)
        and len(student_id) == 7
        and student_id.startswith("CS-")
        and student_id[3:].isdigit()
    )
