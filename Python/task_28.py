
from random import randint


def num_sum(a, b):
    if a == 0:
        return b
    return num_sum(a - 1, b+1)


num_A, num_B = randint(1, 9), randint(1, 9)
print(num_A, num_B)
print(num_sum(num_A, num_B))
