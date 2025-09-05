def set_or_not(n, bit):
    if n & (1 << (bit - 1)):
        return True
    return False


n = int(input("Enter the number: "))
bit = int(input("Enter the bit: "))

is_set = set_or_not(n, bit)

if is_set:
    print("SET")
else:
    print("NOT SET")