"""
    This is for OOP 2.2 Inheritance and Polymorphism
"""

class Dog:
    def __init__(self, average_weight, height_range, life_span, color):
        self.average_weight = average_weight
        self.height_range = height_range
        self.life_span = life_span
        self.color = color

class sportingDog(Dog):
    def __init__(self, average_weight, height_range, life_span, color, sporting_ability):
        super().__init__(average_weight, height_range, life_span, color)
        self.sporting_ability = sporting_ability

    def sport(self):
        return "This dog is a sporting dog!"
    
class nonsportingDog(Dog):
    def __init__(self, average_weight, height_range, life_span, color, sporting_ability):
        super().__init__(average_weight, height_range, life_span, color)
        self.sporting_ability = sporting_ability

    def sport(self):
        return "This dog is a non-sporting dog!"
    
if __name__ == "__main__":
    dachshund = nonsportingDog(average_weight = 20, height_range = "8 inches", life_span = "12 - 16 years", color = "various", sporting_ability = "Not sporty")
    print(f"Dachshund: {dachshund.sport()}")
    dachshund = sportingDog(average_weight = 20, height_range = "8 inches", life_span = "12 - 16 years", color = "various", sporting_ability = "Sporty")
    print(f"Dachshund: {dachshund.sport()}")