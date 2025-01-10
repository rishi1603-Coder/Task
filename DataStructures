
def display_menu():
    print("\n--- Student Management System ---")
    print("1. Add a student")
    print("2. View all students")
    print("3. Update a student")
    print("4. Delete a student")
    print("5. Exit")

def add_student(students):
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grades = input("Enter student grades (comma-separated): ").split(",")
    students[name] = {"age": age, "grades": [grade.strip() for grade in grades]}
    print(f"Student {name} added successfully.")

def view_students(students):
    if not students:
        print("No students found.")
    else:
        for name, info in students.items():
            print(f"\nName: {name}")
            print(f"Age: {info['age']}")
            print(f"Grades: {', '.join(info['grades'])}")

def update_student(students):
    name = input("Enter the name of the student to update: ")
    if name in students:
        print("Enter new details (leave blank to keep current values):")
        age = input(f"Age ({students[name]['age']}): ")
        grades = input(f"Grades ({', '.join(students[name]['grades'])}): ")
        if age:
            students[name]['age'] = int(age)
        if grades:
            students[name]['grades'] = [grade.strip() for grade in grades.split(",")]
        print(f"Student {name} updated successfully.")
    else:
        print(f"Student {name} not found.")

def delete_student(students):
    name = input("Enter the name of the student to delete: ")
    if name in students:
        del students[name]
        print(f"Student {name} deleted successfully.")
    else:
        print(f"Student {name} not found.")

def main():
    students = {}
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            update_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

Output:
--- Student Management System ---
1. Add a student
2. View all students
3. Update a student
4. Delete a student
5. Exit
Enter your choice: 1
Enter student name: rushi
Enter student age: 21
Enter student grades (comma-separated): 97
Student rushi added successfully.

--- Student Management System ---
1. Add a student
2. View all students
3. Update a student
4. Delete a student
5. Exit
Enter your choice: 2

Name: rushi
Age: 21
Grades: 97

--- Student Management System ---
1. Add a student
2. View all students
3. Update a student
4. Delete a student
5. Exit
Enter your choice: 3
Enter the name of the student to update: shiv
Student shiv not found.

--- Student Management System ---
1. Add a student
2. View all students
3. Update a student
4. Delete a student
5. Exit
Enter your choice: 4
Enter the name of the student to delete: rushi
Student rushi deleted successfully.

--- Student Management System ---
1. Add a student
2. View all students
3. Update a student
4. Delete a student
5. Exit
Enter your choice: 2
No students found.

--- Student Management System ---
1. Add a student
2. View all students
3. Update a student
4. Delete a student
5. Exit
Enter your choice:
