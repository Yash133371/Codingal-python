class Student:
    name = "Yash"
    grade = 5
    def introduction(self):
        print("Hello I'm a student")
    def details(self):
        print("Hello my name is", self.name)
        print("I study in grade", self.grade)

ob = Student()
ob.introduction()
ob.details()