def isPowerOf4(n):
    c = 0

    if n > 0:
        while n > 1 :
            n >>= 1
            c += 1
        
        if c % 2 == 0:
            return True
        
        return False
    
    return False


n = int(input("Enter a number: "))

print(f"{n} is a power of 4" if isPowerOf4(n) else f"{n} is not a power of 4")