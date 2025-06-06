class Student:
    def __init__(self, name: str, grade: int):
        self.name = name
        self.grade = grade
        print(f"My name is {self.name}, I'm in grade {self.grade}")

Yash = Student("Yash", 5)