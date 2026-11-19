# Coding exercise only: this does not check a live cohort or waitlist.
def check_cisco_seats(enrolled, max_seats=30):
    if not isinstance(enrolled, int) or enrolled < 0 or enrolled > max_seats:
        return "Invalid enrollment count."
    remaining = max_seats - enrolled
    return "Cohort full (waitlist active)." if remaining == 0 else f"{remaining} seats remaining."
