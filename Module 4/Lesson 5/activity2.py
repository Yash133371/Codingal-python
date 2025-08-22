def ask_number(prompt: str) -> int:
    while True:
        try:
            raw_input = input(prompt)
            result = int(raw_input)
            return result
        except ValueError:
            print("Please enter a valid integer")


largest_number = ask_number("Enter Largest number: ")
smallest_number = ask_number("Enter smallest number: ")

while smallest_number:
    stored_number = smallest_number
    smallest_number = largest_number % smallest_number
    largest_number = stored_number

print("HCF is:", largest_number)