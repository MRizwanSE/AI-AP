from abc import ABC, abstractmethod
from address import Address

class Person(ABC):

    def __init__(self, p_id, name, cnic):    # email=None
        self.p_id = p_id
        self.name = name
        self.cnic = cnic
        # self.email = email
        self.fullAddress = Address()

    # p_id property 
    @property
    def p_id(self):
        return  self.__p_id 
    @p_id.setter
    def p_id(self, value):
        if value is None:
            raise AttributeError("Can't set id attribute")
        if value > 100 or value < 0:
            raise AttributeError("The value is invalid!")
        self.__p_id = value

    # name property
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value

    # cnic property
    @property
    def cnic(self):
        return self.__cnic
    @cnic.setter
    def cnic(self, value):
        self.__cnic = value
    
    # email abstract property
    # @property
    # def email(self):
    #     pass
    
    # @email.setter
    # @abstractmethod
    # def email(self, value):
    #     pass

    # @abstractmethod
    # def info(self):
    #     pass
