def divide(dividend, divisor):
    sign = -1 if dividend < 0 else 1

    dividend = abs(dividend)
    divisor = abs(divisor)

    quotient = 0
    temp = 0

    for i in range(31, -1, -1):
        if temp + (divisor << i) <= dividend:
            temp += divisor << i
            quotient |= 1 << i
    
    if sign == -1:
        quotient = -quotient
    return quotient


a = int(input("Enter a for a / b: "))
b = int(input("Enter b for a / b: "))

print(f"{a} / {b} = {divide(a, b)}")
