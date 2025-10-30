n = int(input("Enter your number: "))

rev = 0

while n != 0:
    rev = (rev << 1) | (n & 1)

    n >>= 1

print(f"Reversed number: {rev} ({bin(rev)[2:]})")