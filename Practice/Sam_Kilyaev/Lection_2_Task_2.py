import random

a = int(random.randint(1, 100))
b = int(random.randint(1, 100))


def more(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    elif b == a:
        print(f"{a} equal {b}")


print(more(a, b))
