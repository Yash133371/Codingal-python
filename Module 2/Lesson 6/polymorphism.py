class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print("Meow!")
    
    def info(self):
        print(f"My name is {self.name}, I'm {self.age} years old and I'm a cat")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print("Woof!")
    
    def info(self):
        print(f"My name is {self.name}, I'm {self.age} years old and I'm a dog")
    
animals = (Dog("Tyson", 8), Cat("Dodo", 2))
for animal in animals:
    animal.info()
    animal.make_sound()