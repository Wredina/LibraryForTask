

from random import randint

n = int(input("введите число арбузов: "))
minNum = 10
maxNum = 1
for i in range(n):
    watermelon = randint(1, 10)
    print(watermelon)
    if watermelon > maxNum:
        maxNum = watermelon
    if watermelon < minNum:
        minNum = watermelon
print(f"max kg {maxNum}")
print(f"min kg {minNum}")
