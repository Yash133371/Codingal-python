class Expression:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
    def __repr__(self):
        return f"Expression({self.num1}, {self.num2}, {self.num3})"
    
    def sum(self):
        return self.num1 + self.num2 + self.num3

obj = Expression(20, 25, 14)
print(obj)
print(obj.sum())