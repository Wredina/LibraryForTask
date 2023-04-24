

from random import randint

size_arr, ran_arr_min, ran_arr_max = randint(9, 15), randint(
    1, 8), randint(8, 16)
print(size_arr, ran_arr_min, ran_arr_max)

arr = [randint(1, 16) for _ in range(size_arr)]
print(arr)

indx_list = [i for i in range(
    size_arr) if ran_arr_min - 1 <= arr[i] <= ran_arr_max]
print(indx_list)
