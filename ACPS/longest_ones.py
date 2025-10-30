n = int(input("Enter your number: "))

most_ones = 0
current_ones = 0

while n != 0:
    bit = n & 1
    
    if bit == 1:
        current_ones += 1
    else:
        current_ones = 0
    
    if current_ones > most_ones:
        most_ones = current_ones
    
    n >>= 1

print(f"Most consecutive ones: {most_ones}")