import unittest
from student.student import Student

class Teststudent(unittest.TestCase):

    def test_create_student_object(self):
        new_student = Student("rahaf")
        self.assertEqual(new_student.name,"rahaf")
