def oddOneOccuring(arr: list):
    res = 0

    for elem in arr:
        res ^= elem
    
    return res


arr = [int(elem) for elem in input("Enter an array: ").split(",")]

res = oddOneOccuring(arr)

print(res, "is the odd one occuring")