# 1

a = int(input("Put in your age here: "))
if 2 > a:
    print("You are a baby")
elif 2 <= a < 4:
    print("You are a kid")
elif 4 <= a < 13:
    print("You are a child")
elif 13 <= a < 20:
    print("You are a teenager")
elif 20 <= a < 65:
    print("You are a grown-up")
else:
    print("You are a senior")


# 2

def move_zeros_to_end(lst):
    return [i for i in lst if i != 0] + [i for i in lst if i == 0]


# Test the function
numbers = [0, 2, 3, 0, 4, 6, 0, 7, 8, 0]
print(move_zeros_to_end(numbers))
