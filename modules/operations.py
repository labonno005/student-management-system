from modules.grades import calculate_grade

FILE = "data/students.txt"


def add_student():
    name = input("Enter Student Name: ")
    age = input("Enter Student Age: ")
    marks = input("Enter Student Marks: ")

    with open(FILE, "a") as file:
        file.write(f"{name},{age},{marks}\n")

    print("Student Added Successfully!")


def view_students():
    try:
        with open(FILE, "r") as file:
            students = file.readlines()

        for student in students:
            name, age, marks = student.strip().split(",")
            print(name, age, marks)

    except FileNotFoundError:
        print("No Student Data Found!")


def search_student():
    search_name = input("Enter Student Name: ").strip().lower()

    with open(FILE, "r") as file:
        students = file.readlines()

    found = False

    for student in students:
        name, age, marks = student.strip().split(",")

        if search_name == name.strip().lower():
            print("\nStudent Found:")
            print("Name:", name)
            print("Age:", age)
            print("Marks:", marks)
            found = True
            break

    if not found:
        print("Student Not Found!")


def update_student():
    name_to_update = input("Enter Student Name: ")

    with open(FILE, "r") as file:
        students = file.readlines()

    updated = False

    with open(FILE, "w") as file:

        for student in students:

            name, age, marks = student.strip().split(",")

            if name.lower() == name_to_update.lower():

                new_name = input("New Name: ")
                new_age = input("New Age: ")
                new_marks = input("New Marks: ")

                file.write(f"{new_name},{new_age},{new_marks}\n")

                updated = True

            else:
                file.write(student)

    if updated:
        print("Student Updated Successfully!")


def delete_student():
    name_to_delete = input("Enter Student Name: ")

    with open(FILE, "r") as file:
        students = file.readlines()

    deleted = False

    with open(FILE, "w") as file:

        for student in students:

            name, age, marks = student.strip().split(",")

            if name.lower() != name_to_delete.lower():
                file.write(student)

            else:
                deleted = True

    if deleted:
        print("Student Deleted Successfully!")
