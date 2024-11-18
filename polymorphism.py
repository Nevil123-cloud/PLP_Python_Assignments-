# Parent Class: Animal
class Animal:
    def move(self):
        pass  # Method to be defined in child classes

# Child Classes: Dog, Bird, Fish
class Dog(Animal):
    def move(self):
        return "The dog is walking 🐕."

class Bird(Animal):
    def move(self):
        return "The bird is flying 🐦."

class Fish(Animal):
    def move(self):
        return "The fish is swimming 🐟."

# Polymorphism in action
animals = [Dog(), Bird(), Fish()]
for animal in animals:
    print(animal.move())
