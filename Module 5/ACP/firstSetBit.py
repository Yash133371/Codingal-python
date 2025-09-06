def first_set_bit(n: int) -> None:
    if n == 0:
        print("0 dosen't have any set bit")
        return
    count = 1
    temp = n
    while temp > 0:
        if temp & 1:
            print("First set bit of", n, "is at place", count)
            break
        count += 1
        temp >>= 1


n = int(input("Enter a number: "))
first_set_bit(n)