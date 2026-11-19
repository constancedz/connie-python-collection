def count_multi_track_students(student_records):
    multi_track_count = 0
    for student, courses in student_records.items():
        if len(courses) > 1:
            multi_track_count += 1
    return multi_track_count
