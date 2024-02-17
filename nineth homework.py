def is_even(number):
    return (number & 1) == 0


print(is_even(2494563894038 ** 2))
print(is_even(1056897 ** 2))
print(is_even(24945638940387 ** 3))


def is_more_even(number_new):
    odd_numbers = [1, 3, 5, 7, 9]
    a = 0
    last_number = str(number_new)[-1]
    return last_number not in odd_numbers


is_more_even_func = is_more_even(44434)
print(is_more_even_func)
