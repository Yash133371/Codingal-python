class Parrot:

    species = "bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sing(self, song):
        print(f"{self.name} is now singing {song}")
    
    def dance(self):
        print(f"{self.name} is now dancing")

blu = Parrot("Blu", 16)
blu.sing("happy")
blu.dance()