#   task   1.1

some_string = input("Put your roman number here:")


def roman_to_arabic(some_string):
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    i = 0

    while i < len(some_string):
        if i + 1 < len(some_string) and values[some_string[i]] < values[some_string[i + 1]]:
            total += values[some_string[i + 1]] - values[some_string[i]]
            i += 2
        else:
            total += values[some_string[i]]
            i += 1
    return total


print(int(roman_to_arabic(some_string)))


# task 2


def process_numbers(numbers):
    new_number = int(''.join(map(str, numbers)))
    new_number += 1
    result = list(map(int, str(new_number)))
    return result


print(process_numbers([9, 9, 9, 9, 9]))


#  task 3


def is_palindrome(some_str):
    some_str = some_str.replace("'", "")
    some_str = some_str.replace(",", "")
    some_str = some_str.replace(".", "")
    some_str = some_str.replace("’", "")
    some_str = some_str.replace(" ", "")
    some_str = some_str.lower()
    return some_str == some_str[::-1]


print(is_palindrome("Red roses run no risk, sir, on Nurse’s order."))
