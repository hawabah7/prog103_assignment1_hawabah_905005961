# ============================================================
# PROG103 - PRINCIPLES OF STRUCTURED PROGRAMMING
# Assignment 1: Student Record Management System
# ============================================================
# Student Name  : Hawa Bah
# System Chosen : Student Record Management System
# SDG           : SDG 4 - Quality Education
# Institution   : Limkokwing University of Creative Technology
#                 Sierra Leone
# Semester      : 02 (March 2026 - July 2026)
# ============================================================

# --- Constants ---
PASS_MARK = 50
MAX_GRADE = 100
SCHOOL_NAME = "Limkokwing University - Sierra Leone"

# --- Global student records list ---
students = []


# ============================================================
# FUNCTION 1: Add a new student record
# ============================================================
def add_student():
    """Prompt user to enter student details and add to records."""
    print("\n" + "=" * 50)
    print("       ADD NEW STUDENT RECORD")
    print("=" * 50)

    name = input("Enter Student Full Name       : ").strip()
    student_id = input("Enter Student ID              : ").strip()

    # Validate that name and ID are not empty
    if not name or not student_id:
        print("\n[ERROR] Student name and ID cannot be empty.")
        return

    # Check for duplicate student ID
    for student in students:
        if student["id"] == student_id:
            print(f"\n[ERROR] Student ID '{student_id}' already exists.")
            return

    # Collect subject scores with validation
    subjects = {}
    print("\nEnter marks for 3 subjects (0 - 100):")

    subject_names = ["Mathematics", "English Language", "ICT"]

    for subject in subject_names:
        while True:
            try:
                score = float(input(f"  {subject} score : "))
                if 0 <= score <= MAX_GRADE:
                    subjects[subject] = score
                    break
                else:
                    print(f"  [ERROR] Score must be between 0 and {MAX_GRADE}. Try again.")
            except ValueError:
                print("  [ERROR] Invalid input. Please enter a number.")

    # Build student record dictionary
    student_record = {
        "name": name,
        "id": student_id,
        "subjects": subjects
    }

    students.append(student_record)
    print(f"\n[SUCCESS] Student '{name}' has been added successfully!")


# ============================================================
# FUNCTION 2: Calculate average and determine grade/status
# ============================================================
def calculate_grade(average):
    """Return letter grade based on average score."""
    if average >= 70:
        return "A - Distinction"
    elif average >= 60:
        return "B - Merit"
    elif average >= 50:
        return "C - Pass"
    elif average >= 40:
        return "D - Near Pass"
    else:
        return "F - Fail"


def calculate_average(scores):
    """Calculate and return the average of a list of scores."""
    if len(scores) == 0:
        return 0.0
    return sum(scores) / len(scores)


# ============================================================
# FUNCTION 3: View all student records and results
# ============================================================
def view_all_students():
    """Display all student records with computed results."""
    print("\n" + "=" * 60)
    print(f"         {SCHOOL_NAME}")
    print("              STUDENT RESULT REPORT")
    print("=" * 60)

    if len(students) == 0:
        print("  No student records found. Please add students first.")
        print("=" * 60)
        return

    for index, student in enumerate(students):
        scores = list(student["subjects"].values())
        average = calculate_average(scores)
        grade = calculate_grade(average)
        status = "PASS" if average >= PASS_MARK else "FAIL"

        print(f"\n  Record #{index + 1}")
        print(f"  Student Name : {student['name']}")
        print(f"  Student ID   : {student['id']}")
        print("  " + "-" * 40)
        print("  Subject Scores:")

        for subject, score in student["subjects"].items():
            print(f"    {subject:<22}: {score:.1f}")

        print("  " + "-" * 40)
        print(f"  Average Score : {average:.2f}%")
        print(f"  Grade         : {grade}")
        print(f"  Status        : {status}")
        print("=" * 60)


# ============================================================
# FUNCTION 4: Search student by ID
# ============================================================
def search_student():
    """Search and display a specific student's record by ID."""
    print("\n" + "=" * 50)
    print("           SEARCH STUDENT RECORD")
    print("=" * 50)

    search_id = input("Enter Student ID to search: ").strip()
    found = False

    for student in students:
        if student["id"] == search_id:
            found = True
            scores = list(student["subjects"].values())
            average = calculate_average(scores)
            grade = calculate_grade(average)
            status = "PASS" if average >= PASS_MARK else "FAIL"

            print(f"\n  Student Found!")
            print(f"  Name         : {student['name']}")
            print(f"  ID           : {student['id']}")
            print("  " + "-" * 38)
            print("  Subject Scores:")
            for subject, score in student["subjects"].items():
                print(f"    {subject:<22}: {score:.1f}")
            print("  " + "-" * 38)
            print(f"  Average Score : {average:.2f}%")
            print(f"  Grade         : {grade}")
            print(f"  Status        : {status}")
            break

    if not found:
        print(f"\n  [NOT FOUND] No student with ID '{search_id}' exists.")


# ============================================================
# FUNCTION 5: Display class summary statistics
# ============================================================
def class_summary():
    """Display summary statistics for all students."""
    print("\n" + "=" * 50)
    print("           CLASS SUMMARY STATISTICS")
    print("=" * 50)

    if len(students) == 0:
        print("  No records available for summary.")
        return

    total_students = len(students)
    passed = 0
    failed = 0
    all_averages = []

    for student in students:
        scores = list(student["subjects"].values())
        avg = calculate_average(scores)
        all_averages.append(avg)

        if avg >= PASS_MARK:
            passed += 1
        else:
            failed += 1

    class_average = calculate_average(all_averages)
    highest = max(all_averages)
    lowest = min(all_averages)

    print(f"\n  Total Students Enrolled : {total_students}")
    print(f"  Students Passed         : {passed}")
    print(f"  Students Failed         : {failed}")
    print(f"  Class Average Score     : {class_average:.2f}%")
    print(f"  Highest Average Score   : {highest:.2f}%")
    print(f"  Lowest Average Score    : {lowest:.2f}%")
    print("=" * 50)


# ============================================================
# FUNCTION 6: Delete a student record
# ============================================================
def delete_student():
    """Remove a student record by ID."""
    print("\n" + "=" * 50)
    print("           DELETE STUDENT RECORD")
    print("=" * 50)

    del_id = input("Enter Student ID to delete: ").strip()

    for index, student in enumerate(students):
        if student["id"] == del_id:
            confirm = input(f"  Are you sure you want to delete '{student['name']}'? (yes/no): ").strip().lower()
            if confirm == "yes":
                students.pop(index)
                print(f"\n  [SUCCESS] Record for '{student['name']}' has been deleted.")
            else:
                print("\n  [CANCELLED] Delete operation cancelled.")
            return

    print(f"\n  [NOT FOUND] No student with ID '{del_id}' found.")


# ============================================================
# MAIN MENU - Entry point of the application
# ============================================================
def main_menu():
    """Display the main menu and handle user navigation."""
    print("\n" + "=" * 60)
    print(f"       {SCHOOL_NAME}")
    print("      STUDENT RECORD MANAGEMENT SYSTEM")
    print("              PROG103 Assignment 1")
    print("=" * 60)
    print("  Supporting SDG 4: Quality Education in Sierra Leone")
    print("=" * 60)

    while True:
        print("\n  MAIN MENU")
        print("  ---------")
        print("  [1] Add New Student Record")
        print("  [2] View All Student Records")
        print("  [3] Search Student by ID")
        print("  [4] View Class Summary Statistics")
        print("  [5] Delete Student Record")
        print("  [6] Exit System")
        print()

        choice = input("  Enter your choice (1-6): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_all_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            class_summary()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("\n  Thank you for using Student Record Management System.")
            print("  Goodbye!\n")
            break
        else:
            print("\n  [ERROR] Invalid choice. Please enter a number between 1 and 6.")


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================
if __name__ == "__main__":
    main_menu()