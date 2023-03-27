

n = int(input('введите число: '))
if n == 0 or n == 1:
    print(1)
else:
    i = 1
    res = 1
    while i <= n:
        res = res*i
        i += 1
    print(res)
