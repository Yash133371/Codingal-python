def roman_to_int(roman_input):
    roman = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }

    result_int = 0

    for i in range(0, len(roman_input) - 1):
        if roman[roman_input[i]] < roman[roman_input[i + 1]]:
            result_int -= roman_input[i]
        else:
            result_int += roman[roman_input[i]]
    
    return result_int + roman[roman_input[-i]]


roman = input("Input roman numeral: ")

print(f"Integer equivalent: {roman_to_int(roman)}")