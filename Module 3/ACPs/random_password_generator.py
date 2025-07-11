import random
import string

try:
    length = int(input("Enter the password length: "))
    password = random.choices(
        string.ascii_letters
        + string.digits
        + string.punctuation,
        k=length
    )
    print("".join(password))
except ValueError:
    print("Error length not an integer")