

from random import randint
n = randint(5, 10)
print(n)
k = randint(1, 3)
print(k)
list_1 = [randint(0, 10) for i in range(n)]
print(list_1)
for i in range(k):
    a = list_1.pop()
    list_1.insert(i, a)
print(list_1)
