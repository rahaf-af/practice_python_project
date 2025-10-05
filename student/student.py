class Student:
    def __init__(self,name):
        self.name= name
        self.grades = []

    def add_grade(self, grade):
        if grade >= 0 and grade <=100 :
            self.grades.append(grade)
        else :
            raise ValueError("grade must be between 0 and 100 inclusive")
    def average(self):
        if not self.grades:
            return 0
        total = 0
        for grade in self.grades:
            total += grade
        average = total / len (self.grades)
        return(average)



if __name__ == "__main__":
    student_name = input("enter your name please: ")
    new_student = Student(student_name)
    print(f"welcome {new_student.name}")
    new_grade = input ("add grade to student")
    try:
        new_student.add_grade(int(new_grade))
    except ValueError:
        raise ValueError("grade must be between 0 and 100 inclusive")
    



