# Practice exercise: age ranges are illustrative, not verified placement rules. Use fictional names.
def assign_coding_track(student_name, age):
    if age < 5:
        return f"{student_name} is too young for current Connie sons tracks."
    
    if 5 <= age <= 7:
        return f"{student_name} -> Junior Scratch Track"
    elif 8 <= age <= 13:
        return f"{student_name} -> Scratch & Robotics Track"
    else:
        return f"{student_name} -> Python, Web Dev & IoT Track"
