from create_date import *
from time import sleep


def add_person():
    name = info_user_write()
    take_info = open(
        'D:\программирование\Обучение_тестировщик\Less_1\знакомство_с_Python\\task_49\\tel.txt', 'a', encoding='utf-8')
    take_info.writelines(name)
    take_info.close()


def print_data():
    with open('D:\программирование\Обучение_тестировщик\Less_1\знакомство_с_Python\\task_49\\tel.txt', 'r', encoding='utf-8') as take_info:
        print(take_info.read())
        sleep(5)


def search_user_info():
    search = input('что ищем? ')
    with open('D:\программирование\Обучение_тестировщик\Less_1\знакомство_с_Python\\task_49\\tel.txt', 'r', encoding='utf-8') as take_info:
        print(*list(filter(lambda x: search in x, take_info)))
        sleep(5)


def dell_user():
    dell = input('кого удаляем? ')
    with open('D:\программирование\Обучение_тестировщик\Less_1\знакомство_с_Python\\task_49\\tel.txt', 'r', encoding='utf-8') as take_info:
        text_data = take_info.readlines()
        with open('D:\программирование\Обучение_тестировщик\Less_1\знакомство_с_Python\\task_49\\tel.txt', 'w', encoding='utf-8') as take_info:
            for line in text_data:
                if dell not in line:
                    take_info.writelines(line)
            print('контакт удалён')
            sleep(5)


def change_user():
    num_change = input('''что хоти изменить:
1 - фамилию
2 - имя
3 - отчество
4 - телефон
введите номер: ''')
    user = input('кого меняем? ')
    new_iformation = input('на что меняем? ')
    with open('D:\программирование\Обучение_тестировщик\Less_1\знакомство_с_Python\\task_49\\tel.txt', 'r+', encoding='utf-8') as take_info:
        text_data = take_info.readlines()
        with open('D:\программирование\Обучение_тестировщик\Less_1\знакомство_с_Python\\task_49\\tel.txt', 'w', encoding='utf-8') as take_info:
            for line in text_data:
                if user in line:
                    line = list(line.split())
                    line.pop(int(num_change) - 1)
                    line.insert(int(num_change) - 1, new_iformation)
                    line = ' '.join(line)
                    take_info.writelines(line + '\n')
                else:
                    take_info.writelines(line)
