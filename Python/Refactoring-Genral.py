class Animal:
    def make_sound(self):
        pass  # This method will be overridden by subclasses

class Cat(Animal):
    def make_sound(self):
        return "Meow"

class Dog(Animal):
    def make_sound(self):
        return "Bark"

class Bird(Animal):
    def make_sound(self):
        return "Tweet"
