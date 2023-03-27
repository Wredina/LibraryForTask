# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

def natural_num(num):
    if num <= 1:
        return num
    else:
        for el in range(2, int((num**0.5)+1)):
            if num % el == 0:
                return "no"
            return 'yes'


print(natural_num(97))
