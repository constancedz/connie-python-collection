# Coding exercise: these example age-based tracks are not verified placement criteria.
def assign_connie_sons_track(name, age):
    if not isinstance(age, int) or age < 5:
        return f"Constraint Error: {name} must be at least 5 years old."
    if age <= 7:
        return f"{name}: Junior Scratch & Logic Track"
    elif age <= 13:
        return f"{name}: Scratch, Robotics & GirlCoder Club Track"
    else:
        return f"{name}: Python, Web Dev & Cisco Track"
