#  task 1

a = input("Put your name and age here: (Nick, 13)")
a = a.split(",")


def say_hi(human_name=str(a[0]), human_age=int(a[1])):
    return print(f"Hi! My name is {human_name} and I am {human_age} years old!")


print(say_hi())

# task 2

b = input("Put sentence here:")


def correct_sentence(some_sentence):
    if some_sentence[-1] != ".":
        some_sentence += some_sentence + "."
        return some_sentence.capitalize()
    return some_sentence.capitalize()


print(correct_sentence(b))


# task 3

def second_index(our_string, letter):
    counter = 0
    for i in range(len(our_string)):
        if our_string[i] == letter:
            counter += 1
            if counter == 2:
                return i
    return None


print(second_index("yoooooyoyoyoy", "yo"))


# task 4


def generate_lists(n):
    list1 = [i for i in range(3, 3 * n + 1, 3)]
    list2 = [i for i in range(5, 5 * n + 1, 5)]

    common_elements = set(list1) & set(list2)
    print(list1, list2)
    return common_elements


print(generate_lists(30))

