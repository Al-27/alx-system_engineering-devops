#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if (roman_string is None) or (type(roman_string) is not str):
        return 0

    number = len(roman_string)
    val = roman[roman_string[number-1]]
    for i in range(number - 1, 0, -1):
        current_value = roman[roman_string[i]]
        previous_value = roman[roman_string[i-1]]

        if previous_value >= current_value:
            val += previous_value
        else:
            val -= previous_value

    return val
