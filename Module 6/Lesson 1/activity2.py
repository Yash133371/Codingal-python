def flips(a: int, b: int):
    flip = 0

    while a > 0 or b > 0:
        temp1 = a & 1
        temp2 = b & 1

        if temp1 != temp2:
            flip += 1
        
        a >>= 1
        b >>= 1

    return flip


a, b = map(int, input("Enter two numbers: ").split())

print(flips(a, b))