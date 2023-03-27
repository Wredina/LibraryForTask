"""
"""
# Ваня:
n = int(input())
max_number = 1000  # max_number = n
while n != 0:
    n = int(input())
    if max_number > n:  # max_number < n:
        max_number = n
print(max_number)

# Петя

n = int(input())
max_number = -1
while n < 0:  # n > 0
    n = int(input())  # переместить на 51-ю строчку
    if max_number < n:
        n = max_number  # max_number = n
print(n)  # print(max_number)
