from model import Person

class Teacher(Person):

    def __init__(self, p_id=0, name=None, cnic=None, salary=None):
        super(Teacher, self).__init__(p_id, name, cnic)
        self.salary = salary

    # salary property 
    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        self.__salary = value
