# Format check only: this does not verify the date, checksum, or authenticity.
# Do not use real ID numbers in public examples.
def is_valid_sa_id_format(id_number):
    # Constraint: Must be a string of 13 digits
    if isinstance(id_number, str) and len(id_number) == 13 and id_number.isdigit():
        return True
    return False
