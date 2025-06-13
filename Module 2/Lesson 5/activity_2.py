class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def show_name(self):
        print(self.fname, self.lname)

class Student(Person):
    def __init__(self, fname, lname, graduation_year):
        super().__init__(fname, lname)
        self.graduation_year = graduation_year
    
obj = Student("Joey", "King", 2021)
obj.show_name()
print(obj.graduation_year)