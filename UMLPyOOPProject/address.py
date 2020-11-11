class Address:
    
    def __init__(self, city="Fsd", country="Pak"):
        self.city = city            
        self.country = country

    # city property 
    @property
    def city(self):
        return self.__city;
    @city.setter
    def city(self, value):
        if value is None:
            raise AttributeError("Can't set city name")
        if len(value) < 3:
            raise AttributeError("Invalid city name")
        self.__city = value

    # country property 
    @property
    def country(self):
        return self.__country;
    @country.setter
    def country(self, value):
        self.__country = value
