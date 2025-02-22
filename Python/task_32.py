

# ТУТ 2 ВАРИАНТА РЕШЕНИЯ

# я автоматизировала процесс

from random import randint
size = randint(8, 15)
numX = randint(1, 9)

array = [randint(1, 20) for el in range(size)]
print(array)

# вариант 1 - сколько раз встречается сам Х
count = 0
for item in range(size):
    if numX == array[item]:
        count += 1
print(numX)
print(count)

# вариант 2 - сколько всего Х, даже учитывая двузначные числа
count = 0
for item in range(size):
    # если Х равен числу или Х равен последнему числу или Х равен первому числу
    if numX == array[item] or numX == array[item] % 10 or numX == array[item] // 10:
        count += 1  # увеличиваем счётчик
    # если Х равен первому и Х равен второму числу (если число 11,22,33 и т.д.)
    if numX == array[item] // 10 and numX == array[item] % 10:
        count += 1  # увеличиваем счётчик на 1, т.к. в первом условии уже было увеличение счётчика на 1
print(numX)
print(count)
