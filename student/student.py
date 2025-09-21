class Student:
    def __init__(self,name):
        self.name= name
        self.grades = []


if __name__ == "__main__":
    student_name = input("enter your name please: ")
    new_student = Student(student_name)
    print(f"welcome {new_student.name}")
