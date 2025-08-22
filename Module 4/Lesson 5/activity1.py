def ask_number(prompt: str) -> int:
    while True:
        try:
            raw_input = input(prompt)
            result = int(raw_input)
            return result
        except ValueError:
            print("Please enter a valid integer")


number = ask_number("Enter your number: ")

original_number = number
reversed_number = 0

while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10

if original_number == reversed_number:
    print(f"{original_number} is a palindrome")
else:
    print(f"{original_number} is not a palindrome")