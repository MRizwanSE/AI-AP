from model import Person

class Student(Person):

    def __init__(self, s_id=0, name=None, cnic=None, cgpa=0.0, fee=None):
        super(Student, self).__init__(s_id, name, cnic)
        self.cgpa = cgpa
        self.fee = fee

    # cgpa property 
    @property
    def cgpa(self):
        return self.__cgpa
    @cgpa.setter
    def cgpa(self, value):
        if value is None:
            raise AttributeError("Can't set CGPA")
        if value > 4.0 or value < 0.0:
            raise AttributeError("Invalid CGPA!")
        self.__cgpa = value

    # fee property 
    @property
    def fee(self):
        return self.__fee
    @fee.setter
    def fee(self, value):
        self.__fee = value
