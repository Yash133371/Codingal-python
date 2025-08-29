def is_even(n: int):
    if n ^ 1 == n + 1:
        return True
    return False


n = int(input("Enter a number: "))

if is_even(n):
    print(n, "is even")
else:
    print(n, "is odd")