# Parent Class
class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels

    def move(self):
        print("The vehicle is moving.")

# Child Class
class Car(Vehicle):
    def __init__(self, wheels, brand):
        super().__init__(wheels)  # Inherit wheels from Vehicle
        self.brand = brand

    def move(self):
        print(f"The {self.brand} car is driving 🚗.")

vehicle = Vehicle(4)
vehicle.move() 

car = Car(4, "Toyota")
car.move()  
