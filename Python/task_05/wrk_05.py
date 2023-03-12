

i = int(input('Вагон в который сел Коля: '))
j = int(input('Номер который увидл Коля внутри вагона: '))
if i != j:
    total_wagons = j + i - 1
    print(total_wagons)
else:
    print('Определить вагон невозможно')
