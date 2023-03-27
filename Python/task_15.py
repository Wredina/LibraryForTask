

from random import randint

# НЕСКОЛЬКО ВАРИАНТОВ РЕШЕНИЯ

# Вариант 1
# просто посчитаем сколько монет орлом вверх, потом отнимем их от общего кол-ва монет и получим кол-во монет орлом вниз. Сравним и выведем итог

n = int(input('введите количество монет: '))
count = 0
for i in range(n):
    coin = randint(0, 1)
    print(coin, end=" ")
    if coin == 1:
        count += 1
print()
print(count)
coinDown = n - count
if coinDown == count:
    print('кол-во монет вверх орлом и вверх решкой равны')
elif coinDown > count:
    print(f'наименьшее кол-во = {count}')
elif coinDown == 0 or count == 0:
    print("все монеты лежат одной стороной вверх")
else:
    print(f'наименьшее кол-во = {coinDown}')


# вариант 2
# по идее это более затратное для системы решение, когда сразу в цикле через условия находим все монеты.

n = int(input('введите количество монет: '))
cointUp = 0
coinDown = 0
for i in range(n):
    coin = randint(0, 1)
    print(coin, end=" ")
    if coin == 1:
        cointUp += 1
    else:
        coinDown += 1
print()
print(cointUp)
print(coinDown)

if coinDown == cointUp:
    print('кол-во монет вверх орлом и вверх решкой равны')
elif coinDown > cointUp:
    print(f'наименьшее кол-во = {cointUp}')
elif coinDown == 0 or cointUp == 0:
    print("все монеты лежат одной стороной вверх")
else:
    print(f'наименьшее кол-во = {coinDown}')
