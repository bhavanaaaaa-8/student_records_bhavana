students = {}
def add_student():
    name = input("Enter student name: ")
    marks = int(input("Enter marks (0-100): "))
    if 0 <= marks <= 100:
        students[name] = marks
        print("Student added successfully!")
    else:
        print("Invalid marks!")
def display_students():
    if not students:
        print("No student records found.")
        return
    for name, marks in students.items():
        print(name, "-", marks)
def search_student():
    name = input("Enter student name to search: ")
    if name in students:
        print(name, "-", students[name])
    else:
        print("Student not found!")
def sort_students():
    sorted_students = sorted(
        students.items(),
        key=lambda student: student[1]
    )
    for name, marks in sorted_students:
        print(name, "-", marks)
def highest_score():
    if not students:
        print("No student records found.")
        return
    highest = max(students.values())
    for name, marks in students.items():
        if marks == highest:
            print(name, "-", marks)
while True:
    print("\n--- Student Marks Management ---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Sort by Marks")
    print("5. Find Highest Score")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        sort_students()
    elif choice == "5":
        highest_score()
    elif choice == "6":
        print("Exiting program...")
        break
    else:
        print("Invalid choice!")
