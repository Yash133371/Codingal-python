def natural_sum(n):
    sum = 0
    for i in range(n):
        for _ in range(i):
            sum += 1
    
    return sum


print(natural_sum(30))