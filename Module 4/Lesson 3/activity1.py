def prints(n: float) -> None:
    if n <= 0.01:
        return
    print("Codingal")
    prints(n / 2)
    prints(n / 2)


prints(10.0)