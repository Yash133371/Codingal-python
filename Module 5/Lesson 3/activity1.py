def isEqual(x, y):
    return not x ^ y


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print(f"Equal" if isEqual(x, y) else f"Not equal")