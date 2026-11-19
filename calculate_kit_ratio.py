def calculate_kit_ratio(students, available_kits):
    if available_kits < 1:
        return "Constraint Error: At least 1 robotics kit is required."
    if students < 1:
        return "No students registered for this session."
    
    students_per_kit = students / available_kits
    if students_per_kit <= 2:
        return f"Optimal ratio: {students_per_kit:.1f} students per kit."
    else:
        return f"High sharing ratio ({students_per_kit:.1f} per kit): Rotate groups."
