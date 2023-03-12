

# ТУТ НЕСКОЛЬКО ВАРИАНТОВ РЕШЕНИЯ

# вариант решения 1
number = input("введите шестизначный номер билета: ")
if len(number) > 6 or len(number) < 6:
    print("не правильный номер билета")
else:
    firstSum = 0
    lastNumSum = 0
    for i in number[:3]:
        firstSum += int(i)
    for i in number[-1:-4:-1]:
        lastNumSum += int(i)
    print(firstSum, lastNumSum)

    if firstSum == lastNumSum:
        print(
            f"сумма первых трёх чисел {firstSum} = сумме последних трёх {lastNumSum} - счастливый билет")
    else:
        print(
            f"сумма первых трёх чисел {firstSum} не равна сумме последних трёх {lastNumSum} - обычный билет")

# второй вариант решения
number = int(input("введите шестизначный номер билета: "))
if number > 999999 or number < 100000:
    print("не правильный номер билета")
else:
    firstTreeNum = number // 1000
    lastTreeNum = number % 1000
    firstNumSum = (firstTreeNum // 100) + ((firstTreeNum // 10) %
                                           10) + (firstTreeNum % 10)
    lastNumSum = (lastTreeNum // 100) + ((lastTreeNum // 10) %
                                         10) + (lastTreeNum % 10)
    if firstNumSum == lastNumSum:
        print(
            f"сумма первых трёх чисел {firstNumSum} = сумме последних трёх {lastNumSum} - счастливый билет")
    else:
        print(
            f"сумма первых трёх чисел {firstNumSum} не равна сумме последних трёх {lastNumSum} - обычный билет")
