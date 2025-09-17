"""
    This is for assignment OOP 2.7 Encapsulation
"""

class Car:
    def __init__(self, make, model):
        self.__make = make
        self.__model = model

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, value):
        self.__make = value
    
    @property
    def model(self):
        return self.model

    @model.setter
    def model(self, value):
        self.__model = value

    def cars_make_model(self):
        # Print the car info
        return f"This is a {self.__make} {self.__model}"
    
    def car_info(self):
        return f"Make: {self.__make}, Model: {self.__model}"
        

def direct_change():
    # This function should attempt to directly change car1 info, but since make and model
    # Are made privately, it shouldn't change at all

    car1 = Car("Chevy", "Silverado") # Test car example

    try:
        # Try to directly change the make and model of car1, this should fail
        car1.__make = "Honda"
        car1.__model = "Civic"

        return f"{car1.cars_make_model()}" # Print car1 info output is a Chevy Silverado
    except:
        return "There was an error" # Handle Errors

print(direct_change())

car2 = Car("Mazda", "CX5")
print(car2.car_info())
