# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

def my_revers(num):
    if num <= 0:
        return
    user_num = int(input("введите число "))
    my_revers(num - 1)
    print(user_num, end=" ")


size = int(input("введите число: "))
my_revers(size)


# def f(n):
#     if n == 0:
#         return ''
#     k = int(input())
#     return f(n - 1) + f' {k}'
#     # return f(n - 1) + ' ' + str(k)


# n = int(input())
# print(f(n)[1:])
