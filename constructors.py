
class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand    # Attribute
        self.model = model    # Attribute
        self.battery_life = battery_life  # Attribute

    def call(self, number):
        print(f"Calling {number} using {self.brand} {self.model}...")  # Method

phone = Smartphone("Samsung", "Galaxy S23", "24 hours")
print(phone.brand)  
phone.call("+256700123456")  
