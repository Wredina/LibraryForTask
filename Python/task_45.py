

def sum_del(num):
    sum_a = 1
    for el in range(2, int(num**0.5 + 1)):
        if num % el == 0:
            sum_a += el + num // el
    return sum_a


k = int(input('введите k: '))
for first_num in range(1, k):
    second_num = sum_del(first_num)
    if sum_del(second_num) == first_num and first_num != second_num and first_num > second_num:
        print(first_num, second_num)
