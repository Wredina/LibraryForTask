

from random import randint
size = randint(6, 15)
list_1 = [randint(0, 5) for i in range(size)]
print(list_1)
set_1 = set(list_1)
print(set_1)
print(len(set_1))
