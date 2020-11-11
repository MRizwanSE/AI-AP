from course import Course
from teacher import Teacher
from student import Student

class Batch:
    
    def __init__(self, b_id=None, b_name=None):
        self.b_id = b_id
        self.b_name = b_name
        self.course = Course()
        self.teacher = Teacher()
        # self.student = Student()   # for one student 
        self.students = []           # array of students 

    # b_id property
    @property
    def b_id(self):
        return self.__b_id
    @b_id.setter
    def b_id(self, value):
        self.__b_id = value

    # b_name property
    @property
    def b_name(self):
        return self.__b_name
    @b_name.setter
    def b_name(self, value):
        self.__b_name = value
