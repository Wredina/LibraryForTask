

from random import randint

size_arr = randint(5, 9)
print(size_arr)
arr = [randint(1, 10) for _ in range(size_arr)]
print(arr)

count = 0
for i in range(size_arr):
    for indx in range(i+1, size_arr):
        if arr[i] == arr[indx]:
            count += 1
print(count)
