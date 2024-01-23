# task 1

def count_surnames_by_group(surnames_in_list):
    groups_of_letters = {'A-I': 0, 'J-P': 0, 'Q-T': 0, 'U-Z': 0}
    for surname in surnames_in_list:
        first_fullname = surname.split(" ")
        first_letter = first_fullname[1][0].upper()

        if first_letter in ["J", "K", "L", "M", "N", "P", "O"]:
            groups_of_letters['J-P'] += 1
        elif first_letter in ["Q", "R", "S", "T"]:
            groups_of_letters['Q-T'] += 1
        elif first_letter in ["U", "W", "V", "X", "Y", "Z"]:
            groups_of_letters['U-Z'] += 1
        else:
            groups_of_letters['A-I'] += 1
    return groups_of_letters


surnames = ['John Both', 'Zane Joe', 'Peter Zinc', 'Tony Tetrarch']
groups = count_surnames_by_group(surnames)
print(groups)


#  task 2

def get_first_word(string_input):
    symbols = ['.', ',', ';', ':', '?', '!', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '[', ']', '{',
               '}', '|', '/', '<', '>', '"']
    for symbol in symbols:
        string_input = string_input.replace(symbol, "")
    words = string_input.split()
    return words[0]


string_new = "   ... /// ,,,, Hel'lo, world!"
first_word = get_first_word(string_new)
print(first_word)

#  task 3


def plusssing(my_iterables):
    new_list = []
    for iterable in my_iterables:
        for item in iterable:
            new_list.append(item)
    return new_list


iterables = [[1, 2, 3], {'5': 5}, tuple(), (6, 7), range(8, 10)]
a = plusssing(iterables)
print(a)


#  task 4

def pow_pow(x):
    return x ** 2


def some_gen(begin, n, func):
    result = [begin]
    for i in range(n - 1):
        result.append(func(result[-1]))
    return result


print(some_gen(2, 4, pow_pow))

