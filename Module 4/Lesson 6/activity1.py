from math import sqrt


def ask_number(prompt: str) -> int:
    while True:
        try:
            raw_input = input(prompt)
            result = int(raw_input)
            return result
        except ValueError:
            print("Please enter a valid integer")


n = ask_number("Enter a number: ")

for i in range(2, int(sqrt(n)) + 1):
    if n % i == 0:
        print(n, "is not prime")
        break
else:
    print(n, "is prime")