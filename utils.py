import random


def generate_random_array(size: int, lower_bound: int = 1, upper_bound: int = 100) -> list:
    arr = []

    for _ in range(size):
        arr.append(random.randint(lower_bound, upper_bound))

    return arr


def generate_sequence(size: int, missing: int) -> list:
    arr = []

    for i in range(1, size + 1):
        if i != missing:
            arr.append(i)

    return arr
