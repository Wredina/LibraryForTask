

def load_data():
    with open('D:\программирование\Обучение_тестировщик\Less_1\знакомство_с_Python\\task_49\\tel.txt', 'r+', encoding='utf-8') as take_info:
        text_data = take_info.read()
        adress_file = "D:\программирование\Обучение_тестировщик\Less_1\знакомство_с_Python\\task_49\\new_info.txt"
        with open(adress_file, 'r', encoding='utf-8') as take_info_2:
            for line in take_info_2:
                if line[:-1] not in text_data:
                    take_info.write(line)
