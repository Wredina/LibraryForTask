

from random import randint

size_arr = randint(5, 15)

arr = [randint(1, 5) for i in range(size_arr)]
print(arr)
min_num = min(arr)
max_num = max(arr)

for grade in range(size_arr):
    if arr[grade] == max_num:
        arr[grade] = min_num
print(arr)

# def grade(n):
#     list_1 = []
#     for i in range(n):
#       list_1.append(random.randint(1, 5))
#     print(list_1)
# min_num = min(list_1)
# max_num = max(list_1)
# for i in range(n):
#     if list_1[i] == max_num:
#         list_1[i] = min_num
# print(list_1)

# grade(10)
