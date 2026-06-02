def calculate_grade(mark):
    if mark >= 80:
        return "A+"
    elif mark >= 70:
        return "A"
    elif mark >= 60:
        return "A-"
    elif mark >= 50:
        return "B"
    else:
        return "F"
