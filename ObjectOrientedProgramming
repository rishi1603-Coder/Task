class Student:
    def __init__(self, name, age, grades):
        """
        Initialize a Student object with name, age, and grades.
        :param name: str - The student's name.
        :param age: int - The student's age.
        :param grades: list - A list of grades (numbers).
        """
        self.name = name
        self.age = age
        self.grades = grades

    def display_details(self):
        """Display the student's details."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")

    def calculate_average_grade(self):
        """Calculate and return the average grade."""
        if self.grades:
            average = sum(self.grades) / len(self.grades)
            return round(average, 2)  
        return 0.0

if __name__ == "__main__":
    student = Student(name="John Doe", age=20, grades=[85, 90, 78, 92])
    print("Student Details:")
    student.display_details()
    average = student.calculate_average_grade()
    print(f"Average Grade: {average}")


Output:
PS C:\Users\hp\Desktop\RG> & C:/Users/hp/AppData/Local/Programs/Python/Python312/python.exe c:/Users/hp/Desktop/RG/student_oop.py
Student Details:
Name: John Doe
Age: 20
Grades: [85, 90, 78, 92]
Average Grade: 86.25
