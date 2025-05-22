def factorial(n):
    """# factorial() is already defined so it can use it self in it's definition"""
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter any number: ")) # Get user input and convert into an integer
result = factorial(num) # Get the factorial of the number
print(result)