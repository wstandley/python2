"""
    This is for Assignment OOP 2.6 Abstract Classes
"""

from abc import ABC, abstractmethod

class Milkshake(ABC):
    def __init__(self, size, flavor):
        self.size = size
        self.flavor = flavor

    @abstractmethod
    def adds(self):
            pass

    @abstractmethod
    def description(self):
            pass

class Chocolate(Milkshake):
    def __init__(self, size, flavor):
        super().__init__(size, flavor)

    def adds(self):
            return "Whip Cream"
        
    def description(self):
            return f"Chocolate Milkshake: {self.size}, {self.flavor} Milkshake, with {self.adds()}"
    
class Strawberry(Milkshake):
    def __init__(self, size, flavor):
        super().__init__(size, flavor)

    def adds(self):
            return "Whip Cream and a Cherry on top"
        
    def description(self):
            return f"Strawberry Milkshake: {self.size}, {self.flavor} Milkshake, with {self.adds()}"
        

chocolate_milkshake = Chocolate("Large", "Chocolate")
print(chocolate_milkshake.description())

strawberry_milkshake = Strawberry("Medium", "Strawberry")
print(strawberry_milkshake.description())