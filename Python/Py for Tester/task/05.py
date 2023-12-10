"""
На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.

Напишите программу, которая должна возвращать сумму и произведение дробей.

Для проверки своего кода используйте модуль fractions.
"""

import fractions

frac1 = "1/2"
frac2 = "1/3"

num_a, num_b = frac1.split('/')
num_c, num_d = frac2.split('/')

fr_1 = fractions.Fraction(int(num_a), int(num_b))
fr_2 = fractions.Fraction(int(num_c), int(num_d))

print(fr_1 + fr_2)
print(fr_1 * fr_2)
