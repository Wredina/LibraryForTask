"""


"""


# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n-1) + fib(n-2)


# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i))
# print(list_1)


# def fib(n):
#     if n < 2:
#         return n
#     else:
#         return fib(n-1) + fib(n-2)

# num = int(input('введите число: '))
# fib(num)
# print(fib(num))


def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


num = int(input('введите число: '))
if num == 1:
    print(0)
else:
    print(fib(num - 1))
