

n = int(input("введите число: "))
flag = True
countNum = 1
res = 1
while flag:
    if res < n:
        print(res)
        res = countNum*2
        countNum += 1
    else:
        flag = False
