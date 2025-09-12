def isPowerOf2(n):
    if n == 0:
        return False
    
    if n & ~(n - 1) == n:
        return True
    
    return False


n = int(input("Enter a number: "))

print(f"{n} is a power of 2" if isPowerOf2(n) else f"{n} is not a power of 2")
