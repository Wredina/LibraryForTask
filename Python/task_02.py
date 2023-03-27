

# ТУТ НЕСКОЛЬКО ВАРИАНТОВ РЕШЕНИЯ

# вариант решения 1
userNum = input('введите трёхзначное число: ')

if len(userNum) > 3 or len(userNum) < 3:
    print("вы ввели не верное число")
else:
    sum = 0
    for i in userNum:
        sum += int(i)
    print(sum)

# вариант решения 2
userNum = int(input('введите трёхзначное число: '))
if userNum > 999 or userNum < 100:
    print("вы ввели не верное число")
else:
    firstNum = userNum // 100
    twoNum = (userNum // 10) % 10
    treeNum = userNum % 10
    sumNum = firstNum + twoNum + treeNum
    print(sumNum)
