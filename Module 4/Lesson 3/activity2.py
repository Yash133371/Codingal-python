from collections.abc import Iterable


def array_sum(a: Iterable) -> int:
    sum = 0
    for i in a:
        sum += i
    
    return sum


def sum_(n: int) -> int:
    return n * (n + 1) / 2


def sum__(n: int) -> int:
    if n <= 0:
        return 0
    
    return n + sum__(n - 1)


a = list(range(1, 1 + 10))
print(array_sum(a))
print(sum_(10))
print(sum__(10))