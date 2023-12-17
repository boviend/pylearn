# 1 calc
# do we need some func for that?

while True:
    first_number = float(input("Put your 1st number:"))
    if first_number == "quit":
        break
    first_sign = input("Put your arithmetic sign:")
    if first_sign == "quit":
        break
    second_number = float(input("Put your 2nd number:"))
    if second_number == "quit":
        break
    if first_sign == "+":
        result = first_number + second_number
    elif first_sign == "-":
        result = first_number - second_number
    elif first_sign == "*":
        result = float(first_number) * float(second_number)
    elif first_sign == "/":
        if float(second_number) != 0:
            result = float(first_number) / float(second_number)
        else:
            print("Divided by zero is prohibited")
            continue
    else:
        print("Something went wrong")
        continue

    print(result)

# 2 list divider

my_list = list(input("Put your list_values here: "))

if len(my_list) % 2 == 0:
    # why I cant make first_l_s var as INT?
    first_list_size = len(my_list) // 2
    print([my_list[:first_list_size], my_list[first_list_size:]])
elif len(my_list) % 2 != 0:
    first_list_size = len(my_list) // 2 + 1
    print([my_list[:first_list_size], my_list[first_list_size:]])
elif len(my_list) == 0:
    print(f"list(First half:, {my_list}, Second half: {my_list}) ")

# 3 multiplication

multi_list = input("Put your nums here: ")
if multi_list != '0':
    multi_list_second = list(map(int, multi_list.split()))
    order = 10
    while order > 9:
        order = 1
        for number in multi_list_second:
            order *= number
        if order > 9:
            multi_list_second = list(map(int, str(order)))
    print(order)

# 4 random not random

import random

n = random.randint(3, 10)
my_random = random.sample(range(1, 9999), n)
my_random_filtered = []
my_random_filtered.insert(0, my_random[0])
my_random_filtered.insert(1, my_random[2])
my_random_filtered.insert(2, my_random[-2])
print(my_random)
print(my_random_filtered)


# 5 alphabet

import string

letters_str = input("Put your letters here(a-Z format): ")
letters_list = letters_str.split("-")
list_start = letters_list[0]
list_end = letters_list[1]
start_index = ascii_letters.index(list_start)
end_index = string.ascii_letters.index(list_end)+1
new_list = string.ascii_letters[start_index:end_index]
print(new_list)
