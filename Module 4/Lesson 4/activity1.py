def ask_number(prompt: str) -> int:
    while True:
        try:
            raw_input = input(prompt)
            result = int(raw_input)
            return result
        except ValueError:
            print("Please enter a valid integer")


number = ask_number("Enter a number: ")
digits = len(str(number))
temp = number
result = 0

while temp > 1:
    result += (temp % 10) ** digits
    temp //= 10

if result == number:
    print(f"{number} is an armstrong number")
else:
    print(f"{number} is not an armstrong number")
