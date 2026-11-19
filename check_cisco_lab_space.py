# Coding exercise: capacity is an adjustable example, not a live enrollment check.
def check_cisco_lab_space(enrolled_count, max_capacity=30):
    if enrolled_count < 0 or enrolled_count > max_capacity:
        return "Error: Invalid enrollment count."
    
    seats_left = max_capacity - enrolled_count
    if seats_left == 0:
        return "Cisco Cohort Full: Add student to the waiting list."
    else:
        return f"Seat available! {seats_left} spots remaining."
