class Course:

    def __init__(self, c_id=None, c_name=None, credits=None):
        self.c_id = c_id
        self.c_name = c_name
        self.credits = credits

    # c_id property 
    @property
    def c_id(self):
        return self.__c_id
    @c_id.setter
    def c_id(self, value):
        self.__c_id = value

    # c_name property 
    @property
    def c_name(self):
        return self.__c_name
    @c_name.setter
    def c_name(self, value):
        self.__c_name = value

    # credits
    @property
    def credits(self):
        return self.__credits
    @credits.setter
    def credits(self, value):
        self.__credits = value
