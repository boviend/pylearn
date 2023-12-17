# task 1

dicts = [{'item_yo': 'item1', 'amount1': 500}, {'item_yo': 'item2', 'amount1': 300},
         {'item_yo': 'item1', 'amount1': 750}, {'item_yo': 'item3', 'amount1': 1750}]
# dicts = list(input("put your dicts here:"))

result = {}

for d in dicts:
    item = list(d.keys())[0]
    amount = list(d.keys())[1]

    if d[item] in result:
        result[d[item]] += d[amount]
    else:
        result[d[item]] = d[amount]

print(result)

# task 2

from collections import Counter

s = "huy pizda suka"
# s = input("Put your string here:")
counter = Counter(s)

print(dict(counter))

# task 3


# corteges_super = list(input("put your corteges here:"))
corteges_super = [("you", 10), ("me", 20), ("me", 60)]

dictionary_result = {}

for dr in corteges_super:
    item1 = dr[0]
    amount1 = dr[1]

    if item1 in dictionary_result:
        dictionary_result[item1].append(amount1)
    else:
        dictionary_result[item1] = [amount1]

print(dictionary_result)

# task 4

your_numbers_list = [1, 2, 3, 4, 5]
your_super_number = 5
your_result = []

for i in range(len(your_numbers_list)):
    for j in range(i+1, len(your_numbers_list)):
        first_operand = your_numbers_list[i]
        second_operand = your_numbers_list[j]

        if first_operand + second_operand == your_super_number:
            your_result.append([first_operand, second_operand])

print(your_result)


