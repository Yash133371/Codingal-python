def natural_sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i

    return sum


print(natural_sum(30))