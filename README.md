# Student_-management_system
class Student:
    def __init__(self, student_id, name, branch, semester, marks):
        self.student_id = student_id
        self.name = name
        self.branch = branch
        self.semester = semester
        self.marks = marks

    def display(self):
        print("\nStudent ID:", self.student_id)
        print("Name:", self.name)
        print("Branch:", self.branch)
        print("Semester:", self.semester)
        print("Marks:", self.marks)


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self):
        student_id = input("Enter Student ID: ")
        name = input("Enter Name: ")
        branch = input("Enter Branch: ")
        semester = input("Enter Semester: ")
        marks = float(input("Enter Marks: "))

        student = Student(student_id, name, branch, semester, marks)
        self.students.append(student)
        print("Student Added Successfully!")

    def search_student(self):
        sid = input("Enter Student ID to Search: ")

        for student in self.students:
            if student.student_id == sid:
                print("\nStudent Found:")
                student.display()
                return student

        print("Student Not Found!")
        return None

    def update_student(self):
        sid = input("Enter Student ID to Update: ")

        for student in self.students:
            if student.student_id == sid:
                student.name = input("Enter New Name: ")
                student.branch = input("Enter New Branch: ")
                student.semester = input("Enter New Semester: ")
                student.marks = float(input("Enter New Marks: "))

                print("Student Updated Successfully!")
                return

        print("Student Not Found!")

    def delete_student(self):
        sid = input("Enter Student ID to Delete: ")

        for student in self.students:
            if student.student_id == sid:
                self.students.remove(student)
                print("Student Deleted Successfully!")
                return

        print("Student Not Found!")

    def display_all(self):
        if not self.students:
            print("No Student Records Available!")
        else:
            print("\n----- Student Records -----")
            for student in self.students:
                student.display()


manager = StudentManager()

while True:
    print("\n===== Student Data Manager =====")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display All Students")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == '1':
        manager.add_student()
    elif choice == '2':
        manager.search_student()
    elif choice == '3':
        manager.update_student()
    elif choice == '4':
        manager.delete_student()
    elif choice == '5':
        manager.display_all()
    elif choice == '6':
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")
