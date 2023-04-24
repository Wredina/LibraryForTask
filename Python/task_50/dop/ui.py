import os
from logger import *
from import_data import load_data


def user_interface():
    os.system('cls')
    print('''1 - добавить контакт
2 - поиск контакта
3 - импорт файла
4 - вывод всех контактов
5 - удаление контакта
6 - изменение контакта
7 - выход''')
    user_input = input('введите номер нужной операции: ')
    while user_input != "7":
        if user_input == '1':
            add_person()
        elif user_input == '2':
            search_user_info()
        elif user_input == '3':
            load_data()
        elif user_input == '4':
            print_data()
        elif user_input == '5':
            dell_user()
        elif user_input == '6':
            change_user()
        else:
            print('попробуйте ещё раз')
        os.system('cls')
        print('''1 - добавить контакт
2 - поиск контакта
3 - импорт файла
4 - вывод всех контактов
5 - удаление контакта
6 - изменение контакта
7 - выход''')
        user_input = input('введите номер нужной операции: ')
