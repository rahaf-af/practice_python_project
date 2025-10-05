import unittest
from student.student import Student

class Teststudent(unittest.TestCase):
    def setUp(self):
        self.student =Student("rahaf")

    def test_create_student_object(self):
        #new_student = Student("rahaf")
        self.assertEqual(self.student.name,"rahaf")
    def test_add_valid_grade(self):
        self.student.add_grade(50)
        self.assertIn (50,self.student.grades)
    def test_add_invalid_grade(self):
        with self.student.add_grade(ValueError):
            self.student.add_grade(101)
            self.student.add_grade(-1)
        with self.student.add_grade(TypeError):
            self.student.add_grade("hello")
    def test_average_no_grades(self):
        self.assertEqual(self.student.average(),0)

    def test_average_with_grades(self):
        for grade in [100, 70 ,80]:
            self.student.add_grade(grade)
        self.assertEqual(self.student.average(),40)