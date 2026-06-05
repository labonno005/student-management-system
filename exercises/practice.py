from modules.grades import calculate_grade

marks = [85, 72, 64, 45]

for mark in marks:
    print(f"Marks: {mark} -> Grade: {calculate_grade(mark)}")
