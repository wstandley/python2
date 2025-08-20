# This is for OOP 1.2 Class and Instance Data

class ToyCar:
    toy_type = "car"

    def __init__(self, brand, color, type, motorized):
        self.brand = brand
        self.color = color
        self.type = type
        self.motorized = motorized

    def play(self):
        print("The toy car moves forward.")
    def sound(self):
        print("Vroom")

race_car = ToyCar(brand="Hot Wheels", color="red", type="race car", motorized=True)
pickup_truck = ToyCar(brand="Tonka", color="yellow", type="pickup truck", motorized=False)
police_car = ToyCar(brand="Matchbox", color="blue", type="police car", motorized=True)

print(race_car.__class__)
print(pickup_truck.__class__)
print(police_car.__class__)

print(police_car.__dict__)
