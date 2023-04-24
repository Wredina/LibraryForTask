
from random import randint

num_1, step, size_arr = randint(1, 9), randint(2, 5), randint(5, 9)
print(num_1, step, size_arr)

arr = []
for i in range(size_arr):
    arr.append(num_1)
    num_1 += step
print(arr)
