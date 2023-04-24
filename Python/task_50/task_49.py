# Иванов Иван Иванович 5458798434
# Сидоров Сидр Сидорович 58464322
# Петров Петр Петрович 58764546
# Жесткий Жека Жеканович 876855

# list_1 = list([name, ' ', midleName, ' ', sureName, ' ', number_tel, '\n'])

import os


def info_user_write():
    full_name_phone = list(
        [input('напишите своё ФИО и номер телефона через пробел: '), '\n'])
    take_info = open('task_49\\tel.txt', 'a', encoding='utf-8')
    take_info.writelines(full_name_phone)
    take_info.close()


def read_user_info():
    with open('task_49\\tel.txt', 'r', encoding='utf-8') as take_info:
        print(take_info.read())


def search_user_info():
    search = input('что ищем? ')
    with open('task_49\\tel.txt', 'r', encoding='utf-8') as take_info:
        print(*list(filter(lambda x: search in x, take_info)))
        # for line in take_info:
        #     if search in line:
        #         print(line)


def load_data():
    with open('task_49\\tel.txt', 'r+', encoding='utf-8') as take_info:
        text_data = take_info.read()
        adress_file = "task_49\\new_info.txt"
        with open(adress_file, 'r', encoding='utf-8') as take_info_2:
            for line in take_info_2:
                if line[:-1] not in text_data:
                    take_info.write(line)


def ui():
    os.system('cls')
    print('''1 - добавить контакт
2 - поиск контакта
3 - ипорт файла
4 - вывод всех контактов
5 - выход''')
    user_input = input('введите номер нужной операции: ')
    while user_input != "5":
        if user_input == '1':
            info_user_write()
        elif user_input == '2':
            search_user_info()
        elif user_input == '3':
            load_data()
        elif user_input == '4':
            read_user_info()
        else:
            print('попробуйте ещё раз')
        os.system('cls')
        print('''1 - добавить контакт
2 - поиск контакта
3 - ипорт файла
4 - вывод всех контактов
5 - выход''')
        user_input = input('введите номер нужной операции: ')


def main():
    ui()


if __name__ == "__main__":
    main()

# info_user_write()
# read_user_info()
# search_user_info()
# load_data()
