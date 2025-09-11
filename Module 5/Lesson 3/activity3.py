def printTwoOdd(arr, size):
    xorof2 = arr[0]

    x = 0
    y = 0
    
    bit = 0

    for i in range(1, size):
        xorof2 ^= arr[i]
    
    setbit = xorof2 & ~(xorof2 - 1)

    for i in range(size):
        if arr[i] & setbit:
            x ^= arr[i]
        else:
            y ^= arr[i]
    
    print("The two odd elements are", x, "and", y)


arr = [int(elem) for elem in input("Enter an array: ").split(",")]

printTwoOdd(arr, len(arr))