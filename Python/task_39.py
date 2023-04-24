

from random import randint

size_arr_1 = randint(5, 9)
size_arr_2 = randint(5, 9)
arr_1 = [randint(1, 9) for i in range(size_arr_1)]
print(arr_1)
arr_2 = [randint(1, 5) for i in range(size_arr_2)]
print(arr_2)
result_arr = [el for el in arr_1 if el not in arr_2]
print(result_arr)
