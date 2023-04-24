

from random import randint

size_arr = randint(5, 9)
print(size_arr)
arr = [randint(1, 10) for _ in range(size_arr)]
print(arr)

count = 0
for i in range(1, size_arr-1):
    if arr[i-1] < arr[i] > arr[i+1]:
        count += 1
print(count)
