

from random import randint

size = randint(6, 10)
bushes = [randint(1, 10) for _ in range(size)]
print(bushes)

max_blueberries = bushes[-1] + bushes[-2] + bushes[0]
sum_tree_bushes = max_blueberries

for i in range(size - 1):
    sum_tree_bushes = bushes[i] + bushes[i-1] + bushes[i+1]
    if sum_tree_bushes > max_blueberries:
        max_blueberries = sum_tree_bushes
print(max_blueberries)

# var_n = int(input("Введите число кустов: "))
# list_berry = []
# for i in range(var_n):
#     list_berry.append(randint(5, 20))
# print(list_berry)
# sum_berry = [list_berry[i] + list_berry[i+1] + list_berry[i+2]
#              for i in range(-2, len(list_berry) - 2)]
# print(sum_berry)
# max_berry = max(sum_berry)
# print(f"Наибольшее число:", max_berry)
