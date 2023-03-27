

num1 = int(input("загадайте 2 числа, напишите их сумму: "))
num2 = int(input("а теперь напишите их произведение: "))

numX = 0
numY = 0
for _ in range(num1):
    numX = num1 - numY
    if numX*numY == num2:
        break
    else:
        numY += 1

print(numX)
print(numY)
