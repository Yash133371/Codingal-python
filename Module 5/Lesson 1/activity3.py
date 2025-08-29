def number_of_bits(n: int):
    count = 0
    while n:
        count += 1
        n >>= 1
    return count


n = int(input("Enter a number: "))
print(n, "is made of", number_of_bits(n), "bits")