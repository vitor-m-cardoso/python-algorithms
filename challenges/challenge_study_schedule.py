def validate_study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    for student_period in permanence_period:
        if student_period[0] is None or student_period[1] is None:
            return None
        if not isinstance(student_period[0], int) or not isinstance(
            student_period[1], int
        ):
            return None
    return True


def study_schedule(permanence_period, target_time):
    valid_schedule = validate_study_schedule(permanence_period, target_time)
    if not valid_schedule:
        return None
    counter = 0
    for student_period in permanence_period:
        if (
            student_period[0] <= target_time
            and student_period[1] >= target_time
        ):
            counter += 1
    return counter
