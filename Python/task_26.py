

from random import randint


def exp(num_A, num_B):
    if num_B == 1 or num_A == 1:
        return num_A
    else:
        return num_A * exp(num_A, num_B - 1)


a = 3
b = 5
print(a, b)
print(exp(a, b))
