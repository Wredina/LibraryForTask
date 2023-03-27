

from random import randint

n = int(input("введите число: "))
maxTemp = 0
count = 0
for i in range(n):
    rndTemp = randint(-50, 50)
    print(rndTemp)
    if rndTemp < 0:
        maxTemp = 0
    if rndTemp > 0:
        maxTemp += 1
        if maxTemp > count:
            count = maxTemp

print(f"кол-во тёплых дней = {count}")
