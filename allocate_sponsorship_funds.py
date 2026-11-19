# Coding exercise: allocations are illustrative, not an approved spending plan.
# Rounding each amount separately may leave a difference of a few cents.
def allocate_sponsorship_funds(total_zar):
    if total_zar <= 0:
        return "Invalid sponsorship amount."
    
    equipment = total_zar * 0.50
    student_data = total_zar * 0.30
    operations = total_zar * 0.20
    
    return {
        "Robotics & Hardware (50%)": f"R{equipment:.2f}",
        "Student Data & Resources (30%)": f"R{student_data:.2f}",
        "Facilitator & Operations (20%)": f"R{operations:.2f}"
    }
