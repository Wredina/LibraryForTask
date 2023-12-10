# Напишите небольшую программу, которая запрашивает у пользователя любой текст и выводит о нём следущую информацию:
# тип объекта
# адрес объекта в оперативной памяти
# хеш объекта

user_txt = input('text ')
user_num = int(input('num '))
user_float_num = float(input('float num '))
print(type(user_txt), id(user_txt), hash(user_txt))
print(type(user_num), id(user_num), hash(user_num))
print(type(user_float_num), id(user_float_num), hash(user_float_num))
