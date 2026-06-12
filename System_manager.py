class Student:
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course

    def display(self):
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Course: {self.course}")
        print("-" * 20)


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self):
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        course = input("Enter Course: ")

        student = Student(student_id, name, course)
        self.students.append(student)

        print("Student Added Successfully!")

    def search_student(self):
        student_id = input("Enter Student ID to Search: ")

        for student in self.students:
            if student.student_id == student_id:
                print("\nStudent Found:")
                student.display()
                return

        print("Student Not Found!")

    def update_student(self):
        student_id = input("Enter Student ID to Update: ")

        for student in self.students:
            if student.student_id == student_id:
                student.name = input("Enter New Name: ")
                student.course = input("Enter New Course: ")
                print("Student Updated Successfully!")
                return

        print("Student Not Found!")

    def delete_student(self):
        student_id = input("Enter Student ID to Delete: ")

        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print("Student Deleted Successfully!")
                return

        print("Student Not Found!")

    def display_students(self):
        if len(self.students) == 0:
            print("No Student Records Found!")
        else:
            print("\nAll Student Records:")
            for student in self.students:
                student.display()


manager = StudentManager()

while True:
    print("\n===== STUDENT DATA MANAGER =====")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display All Students")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

    if choice == '1':
        manager.add_student()
    elif choice == '2':
        manager.search_student()
    elif choice == '3':
        manager.update_student()
    elif choice == '4':
        manager.delete_student()
    elif choice == '5':
        manager.display_students()
    elif choice == '6':
        print("Thank You!")
        break
    else:
        print("Invalid Choice! Try Again.")
