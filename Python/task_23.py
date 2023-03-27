

from random import randint
n = randint(5, 10)
list_1 = [randint(0, 10) for i in range(n)]
print(list_1)
count = 0
for i in range(1, len(list_1)):
    if list_1[i] >= list_1[i - 1]:
        count += 1
print(count)
