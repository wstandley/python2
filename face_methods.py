"""
    This is for Assignment OOP 2.5 Different Faces of Python Methods
"""

class Car:

    def __init__(self, make, model):
        self.make = make
        self.model = model

    # Instance Method
    def car_model(self):
        return f'This car is a {self.model}.'
    
    # Class Method
    @classmethod
    def set_year(cls, year):
        cls.year = year

    # Static Method
    @staticmethod
    def vroom():
        return 'Cars go vroom!'
    

car1 = Car('Toyota', 'Corolla')
car2 = Car('Mazda', 'CX5')
car3 = Car('Ford', 'F150')

# Instance Output
print(car1.car_model())
print(car2.car_model())
print(car3.car_model())
"""
    The instance method uses self. to pull the instances info and obtains whatever is entered
"""

# Class Output
Car.set_year('2025')
print(Car.year)
"""
    The class method uses cls. to obtain and modify a group of attributes and apply it to the whole class and not just the instance
"""

# Static Output
print(Car.vroom())
"""
    The static method allows us to create a function that is able to represent the class as whole that won't need to be modified
"""

"""
    Instance methods are used for individual cases, in my assignments case this would be each individual car. So it can differentiate each individual car.

    Class methods are used to access or modify the group of instances. In my example, each car was made in the year 2025, and that was all 3 of them, not just one otherwise that would be an instance

    Static methods are used to write a function that would relate to everything in the class. Most of the time, this would be unchanging.
"""

