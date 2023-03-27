

def print_field(field):
    print(*field[:3])
    print(*field[3:6])
    print(*field[6:])


def win(field):
    if (my_field[0] == my_field[1] == my_field[2]
        or my_field[3] == my_field[4] == my_field[5]
        or my_field[6] == my_field[7] == my_field[8]
        or my_field[0] == my_field[3] == my_field[6]
        or my_field[1] == my_field[4] == my_field[7]
        or my_field[0] == my_field[4] == my_field[8]
        or my_field[2] == my_field[4] == my_field[6]
            or my_field[2] == my_field[1] == my_field[2]):
        return True
    return False


my_field = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
print_field(my_field)

for step in range(1, 10):
    print(f"{step}-й ход")
    print_field(my_field)
    move = input('Сделайте ход: ')
    while move not in my_field:
        print('не корректный ввод')
        move = input('Сделайте ход: ')
    if step % 2 != 0:
        symbol = '0'
        my_field[int(move) - 1] = symbol
    else:
        symbol = "Х"
        my_field[int(move) - 1] = symbol
    if win(my_field):
        print_field(my_field)
        print(f'вы победун {symbol}')
        break
    else:
        print("ничья")
