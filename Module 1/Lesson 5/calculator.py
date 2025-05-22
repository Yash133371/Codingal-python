def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a/ b

num1 = int(input("Enter number one: "))
num2 = int(input("Enter number two: "))

print(f"Sum: {add(num1, num2)}")
print(f"Difference: {subtract(num1, num2)}")
print(f"Product: {multiply(num1, num2)}")
print(f"Quotient: {divide(num1, num2)}")