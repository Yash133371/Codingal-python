def ones_and_zeros(n):
    ones = 0
    zeros = 0
    while n != 0:
        if n & 1 == 1:
            ones += 1
        else:
            zeros += 1
        
        n >>= 1
    
    return ones, zeros


n = int(input("Enter a number: "))
ones, zeros = ones_and_zeros(n)
print("Ones:", ones, "Zeros:", zeros)