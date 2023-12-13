# def check_date(date_string):
#     day, month, year = date_string.split('.')
#     # Проверка, что компоненты являются числами
#     if not (day.isdigit() and month.isdigit() and year.isdigit()):
#         return False
#     day = int(day)
#     month = int(month)
#     year = int(year)
#     if day <= 0 or month <= 0 or year <= 0:
#         return False
#     # Проверка дня
#     elif month in [1, 3, 5, 7, 8, 10, 12]:
#         if not (1 <= day <= 31):
#             return False
#     elif month in [4, 6, 9, 11]:
#         if not (1 <= day <= 30):
#             return False
#     elif month == 2:
#         # Проверка на високосный год
#         if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#             if not (1 <= day <= 29):
#                 return False
#         else:
#             if not (1 <= day <= 28):
#                 return False
#     else:
#         return False
#     # Проверка месяца
#     if not (1 <= month <= 12):
#         return False
#     # Проверка года
#     if year <= 0:
#         return False
#     return True


# date_to_prove = "15.4.2023"

# print(check_date(date_to_prove))

# queens = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)]

# # Введите ваше решение ниже


# def is_attacking(q1, q2):
#     if q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1]):
#         return True
#     else:
#         return False


# def check_queens(queens):
#     for i in range(len(queens)):
#         for j in range(i+1, len(queens)):
#             if is_attacking(queens[i], queens[j]):
#                 return False
#     return True


# if check_queens(queens):
#     print("True")
# else:
#     print("False")


# import random


# def generate_boards():
#     board_list = []  # список для хранения успешных расстановок ферзей
#     while len(board_list) < 4:  # выполнить 4 раза для каждой успешной расстановки
#         board = []  # текущая расстановка ферзей
#         while len(board) < 8:
#             x = random.randint(0, 7)  # случайная координата по оси x
#             y = random.randint(0, 7)  # случайная координата по оси y
#             # проверка, что координаты не совпадают с уже существующими и не находятся на одной вертикали, горизонтали или диагонали
#             if all(x != c[0] and y != c[1] and abs(x - c[0]) != abs(y - c[1]) for c in board):
#                 board.append((x, y))  # добавить координату в список board
#         # добавить успешную расстановку в список board_list
#         board_list.append(board)
#     return board_list


# print(generate_boards())

from super_module import *

SIZE = 49.5

print(f'{SIZE = }\n{result = }')
print(f'{z = }')  # NameError: name 'z' is not defined
print(f'{_secret = }')  # NameError: name '_secret' is not defined
print(f'{func(100, 200) = }\n{randint(10, 20) = }')


def func(a: int, b: int) -> int:
    return a + b


print(f'{func(100, 200) = }')
