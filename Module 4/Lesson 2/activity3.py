def on_square_time(n):
    for _ in range(n):
        for _ in range(n):
            pass

    print("The number of iterations taken for n =", n, "is", n**2)


on_square_time(5)
on_square_time(4)
on_square_time(3)

print("With every 'n' the time taken is n^2")