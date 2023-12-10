import pandas as pd # импорт модуля pandas и сохранение как pd
from datetime import datetime # импорт datetime из модуля datetime

df = pd.read_csv('lesson_1_data.csv', encoding='windows-1251', sep = ';')  # функция считывания внешнего файла формата csv (можно выбрать необходимый формат)
# первый параметр обязательный - путь к файлу, второй обязательный параметр - разделитель sep
# encoding – параметр в read_csv, отвечает за кодировку текста, которая может быть различной. Самая распространённая – utf
# parse_dates – указывает, стоит ли воспринимать даты как даты (по умолчанию они воспринимаются пандасом как строки).
# пример pd.read_csv(path, parse_dates=['some_date', 'another_date'])
# Параметр с датами может принимать несколько значений:
# True – пытается перевести в дату первую колонку
# список колонок – пытается перевести в дату указанные в списке колонки
# And create_data, payment_data columns will be treated as data
# pd.read_csv('path_to_your.csv', encoding='Windows-1251', sep=';', parse_dates=['create_data', 'payment_data'])

pd.set_option('display.max_columns', None) # убирает ограничение вывода количества столбцов на экран
pd.set_option('display.max_rows', None)    # убирает ограничение вывода количества строк на экран
pd.set_option('display.width', 300)        # подгоняет ширину дисплея
print(df.head())    # выводит первые 5 строк нашей таблицы
print(df.tail())    # выводит последние 5 строк нашей таблицы
print(df.shape)     # выведет (292, 8) - количество строк и количество колонок
print(df.shape[0]) # выведет количество строк
print(len(df)) # выведет количество строк
print(df.shape[1]) # выведет количество колонок


# Series - это маркированная одномерная структура данных, ее можно представить, как таблицу с одной строкой
# DataFrame – это двумерная маркированная структура. По сути таблица
print(df.dtypes) # выведет типы данных по каждой колонке
# Номер                  int64
# Дата создания         object
# Дата оплаты           object
# Title                 object
# Статус                object
# Заработано           float64
# Город                 object
# Платежная система     object
# dtype: object
print(df.describe()) # выводит аналитические показатели - count, mean, std, min, 25%, 50%, 75%, max
print(df.columns) # выведет колонки - Index(['Номер', 'Дата создания', 'Дата оплаты', 'Title', 'Статус', 'Заработано', 'Город', 'Платежная система'], dtype='object')
df = df.rename(columns={'Номер': 'number', # rename - переименовываем колонки таблицы columns
          'Дата создания' : 'create_date',
          'Дата оплаты' : 'payment_date',
          'Title' : 'title',
          'Статус' : 'status',
          'Заработано' : 'money',
          'Город' : 'city',
          'Платежная система' : 'payment_system'})
print(df.head())
# Rename index (row names)
# df = df.rename(index={0: 'Ivanov', 1: 'Vasilev'}) - пример переименования лэйблов строк из 0 в Ivanov и из 1 в Vasilev:


print(df['title'].head()) # выведет колонку title (метод head позволяет вывести только первые 5 стр.)
print(df[['title', 'status']].head()) # выведет колонку title и status (метод head позволяет вывести только первые 5 стр.)
print(df.city.head()) # выведет колонку city (метод head позволяет вывести только первые 5 стр.), работает если название колонки без пробелов

all_money = round(df.money.sum(), 2)  # лайфхак - сохранить общую сумму денег в самом начале работы
print(all_money)

# Задача - 1) найти суммарное количество всех заработанных денег по каждому из курсов
# 2) проранжировать эти курсы по количеству заработанных денег
# 3) Посмотреть разбивку по городам

#money_by_city=df \                               # \ - служит переносом в коде. создаем переменную в которую сохраняем нашу группировку - суммарное количество всех заработанных денег по каждому из курсов
#        .groupby('title', as_index=False) \      # groupby('title', as_index=False) - Группирируем по названиям из колонки 'title', as_index=False - что бы колонка 'title' не была индексом DataFrame(таблицы)
#        .aggregate({'money': 'sum'}) \           # aggregate({'money': 'sum'}) - функция ссумирует, сковывает наши данные, {'money': - это ключ, а 'sum'} - это функция которую хотим применить к нашей колонке
#        aggregate можно заменить на agg
#        .sort_values('money', ascending=False)   # .sort_values('money') - сортируем по нужной нам колонке 'money', ascending=False - позволяет сортировать от большего к меньшему
#   .idxmin – индекс минимального значения
#   .idxmax – индекс максимального значения
money_by_city=df \
    .groupby(['title', 'city'], as_index=False)\
    .aggregate({'money': 'sum'})\
    .sort_values('money', ascending=False)
# groupby('title', as_index=False) - Группирируем по названиям из колонок 'title' и 'city'
print(money_by_city)

money_by_city.to_csv('money_by_city.csv', index=False) # - переменную money_by_city сохраняем (.to_csv ) в формат csv, в качестве аргумента ('money_by_city.csv') - название файла
# index=False - убирает индексы отдельной колонкой
print()
# Задача - 1) сколько суммарных денег 2) сколько завершенных заказов

money_by_title=df  \
    .query("status == 'Завершен'")\
    .groupby('title', as_index=False)\
    .aggregate({'money': 'sum', 'number': 'count'})\
    .sort_values('money', ascending=False)\
    .rename(columns={'number': 'success_orders'})
# .query('number > 1064620')\ - отфильтрует группировку по столбцу 'number' по значениям > 1064620
# .query("status == 'Завершен'")\ - отфильтрует группировку по столбцу status со значениями Завершен
# .aggregate({'money': 'sum', 'number': 'count'})\ - добавляется еще одна колонка 'number'  и применяемая к ней функция count)
# .rename(columns={'number': 'success_orders'}) - переименовывает колонку 'number' в 'success_orders'
# .rename(columns=lambda x: x.replace(' ', '_'), inplace=True) - заменяет пробелы на _ в названиях столбцов
bookings.columns = bookings.columns.str.replace(" ","_").str.lower() #- заменяет пробелы на _ в названиях столбцов и все названия с маленькой буквы
bookings.columns = [(column.lower()).replace(' ', '_') for column in bookings.columns] # - тоже
bookings.columns = bookings.rename(str.lower, axis='columns').columns.str.replace(' ', '_') #- тоже
bookings.columns = bookings.columns.str.lower().str.split().str.join('_') # - тоже

print(money_by_title)
print()

# Задача - проверка - 1) проверить данные на логическую непротиворечивость
print(df.title.unique()) # .unique вернет уникальные позиции из столбца title - сверимся и там и там получается 6 курсов

print(money_by_title.money.sum(), 'равняется ', all_money, '?' ) # переменная money_by_title с помощью sum суммирует все значения в столбце money

print('OK' if money_by_title.money.sum() == all_money else 'ERROR!!!!')

today_day = datetime.today().strftime('%Y-%m-%d') # создает переменную с сегодняшней датой
print(today_day )
file_name ='money_title_{}.csv' # {} используются для функции format
file_name = file_name.format(today_day) # мы получим сразу в названии файла дату, в которую сделана выгрузка - с помощью format() на место {} вставляется значение переменной today_day
print(file_name)
if money_by_title.money.sum() == all_money:
    print('OK! File {} is written'.format(file_name))
    money_by_title.to_csv(file_name, index = False) # если совпали суммы, тогда мы берем файл money_by_title и сохраняем его в формате csv
else:
    print('ERROR!')

    Метод value_counts

# df['name'].value_counts() - сколько раз встречается каждое уникальное значение переменной
# метод value_counts принимает на вход несколько параметров:
# normalize – показать относительные частоты уникальных значений (по умолчанию равен False).
# dropna – не включать количество NaN (по умолчанию равен True)
# bins – сгруппировать количественную переменную (например, разбить возраст на возрастные группы); для использования данного параметра необходимо указать, на сколько групп разбить переменную

# Пример 1
# 1) Получаем частоту встречаемости (напр. Persik – в 40% наблюдений),  также не удаляем из результата NaN:
#df['name'].value_counts(normalize=True, dropna=False)
#Persik    0.4
#Tolya     0.2
#Barsik    0.2
#NaN       0.2
#Name: name, dtype: float64
# 2) Разбиваем year на 2 промежутка:
#df['year'].value_counts(bins=2)
#(2017.5, 2020.0]      3
#(2014.994, 2017.5]    2
#Name: year, dtype: int64

     Метод query - фильтр
#В query также можно передать сразу несколько условий. Условия, которые должны выполняться одновременно, соединяются с помощью and или &:
#product_data.query("title == 'Курс обучения «Эксперт»' and status == 'Завершен'")
#Когда должно удовлетворяться одно из условий – or или |:
#product_data.query("title == 'Курс обучения «Эксперт»' or status == 'Завершен'")
# success_number[success_number.client >30000] - еще один способ прописывать фильтр
# - выведет дата фрейм success_number только те строки, в которых по столбцу client значения будут больше 30000

     Модуль datetime

# datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S') -  Чтобы перевести его в строку сделайте следующее:
# Метод strftime форматирует дату в соответствии с переданным в него форматом:
# % – обозначает, что далее следует часть даты
# Y – год четырьмя знаками
# m – месяц двумя знаками
# d – день
# H - время
# M – минуты
# S – секунды
#Можно использовать только часть фрагментов даты, разделители между ними – на ваше усмотрение (в примере это - и :). Несколько примеров:
#from datetime import datetime
# current date and time
#now = datetime.now()
#print(f'Full time format of now is {now}')
#Full time format of now is 2020-06-01 17:54:40.010540
# Year
#year = now.strftime("%Y")
#print("year:", year)
#year: 2020
# Month
#month = now.strftime("%m")
#print("month:", month)
#month: 06
# Day
#day = now.strftime("%d")
#print("day:", day)
#day: 01
# Time
#time = now.strftime("%H:%M:%S")
#print("time:", time)
#time: 17:54:40
# Date and time
#date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
#print("date and time:",date_time)
#date and time: 06/04/2020, 17:54:40


        Создание своих функций def
#def temp_to_celcius(f):
#    Celsius = (f-32)*5/9
#    return Celsius
#temp_to_celcius(taxi.temp) - вызываем функцию temp_to_celcius и в качестве аргумента указываем столбец temp датафрейма(таблицы) taxi - это позволяет библиотека pandas
#
       Пример с функцией apply:
# def split_brand(brand_name_data):
#     return brand_name_data.split()[-1]
# print(user_df.brand_info.apply(split_brand)) - функция apply говорит - в файле user_df применить к колонке brand_info функцию split_brand
# можно применить ко всему дата фрейму
#
       то же самое с помощью lambda
# user_df.brand_info.apply(lambda x: x.split()[-1])  - функция apply говорит - в файле user_df применить к колонке brand_info функцию lambda со значениями x

    Полезные функции pandas
# users_purchases.purchases.median() - медиана для колонки purchases в дата фрейме users_purchases
# users_purchases.purchases.mean() - ср. ариф. для колонки purchases в дата фрейме users_purchases
# unique() – метод, возвращающий уникальные значения в колонке. Уникальные значения возвращаются в форме array
# nunique() – метод, считающий уникальные значения в колонке
# value_counts() - метод,считающий количество уникальных значений в серии - в единицах
# value_counts(normalize=True) - метод,считающий количество уникальных значений в серии - в процентах (пример -0.247)
# user_df.agg({'brand_name': pd.Series.nunique})
# x =pd.Series([1,2,3]) - пандасовская серия - Series - более продвинутый список для аналитики, со своими методами
# pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A') - добавит новую 3 новых строки с одним столбцом под навзванием 'Product A'
# каждая колонка в дата фрейме это пандосовская серия, только если мы применяем к отдельной колонке, то записываем методы со скобками nunique()
# nunique метод пандосовской серии - Series пандосовский
# дата фрейм - это словарь где ключами словаря являются название колонок, а значениями словаря являются сами колонки
d = pd.DataFrame({'x': [1,2,3], 'y': ['a', 'b', 'c']}) # получается дата фрейм
print(d)

       Объединение датафреймов
users_purchases.merge(user_unique_brands, on = 'user_id') #- функция объединения merge прибавляет
# к дата фрейму users_purchases дата фрейм user_unique_brands, при этом how= по умолчанию inner - это значит,
# что из дата фрейма А и дата фрейма B берутся только те значения, которые есть в обоих таблицах
# how – как объединять датафрэймы, возможные варианты: inner, outer, left, right
# on - общая колонка, по которой будет происходить объединение
# how= 'outer'  - мы бы взяли всех и из А и из В дата фрейма
# how= 'left'  - мы бы взяли всех из А и из В дата фрейма взяли бы те позиции, что есть в дата фрейме А
# how= 'right'  - мы бы взяли всех из B и из A дата фрейма взяли бы те позиции, что есть в дата фрейме B
# users_purchases.merge(user_unique_brands, left_on='user_id', right_on ='id_user') # - left_on и right_on - на случай, если название колонок разное
left.join(right, lsuffix='_CAN', rsuffix='_UK') # - при условии, что индексы одинаковые, соединяем
# датафрейм right к датафрему left, где индексы всё те же общие колонки,
# - если индексы разные, то нужно привести к одним и тем же индексам
# left = canadian_youtube.set_index(['title', 'trending_date']) # сделали датафрейм где индексами выступают колонки 'title', 'trending_date'
# right = british_youtube.set_index(['title', 'trending_date']) # сделали датафрейм где индексами выступают колонки 'title', 'trending_date'
# left.join(right, lsuffix='_CAN', rsuffix='_UK') # соединили датафрейм right к датафрему left, где индексы всё те же общие колонки,
# а далее идут сначала колонки из датафрейма left и к названиям колонок прибавляется суфикс '_CAN'
# , затем правые и к названиям колонок прибавляется суфикс '_UK'


loyalty_df[loyalty_df.unique_brands == 1] # метод фильтрации - в дата фрейме loyalty_df фильтруем по колонке loyalty_df.unique_brands,
# # выбирая только строки  со значением 1

       Индекс и имена колонок
# У датафрэйма есть два атрибута – index и columns.  Они позволяют получить доступ к соответствующей информации в виде array (на самом деле не совсем array)
#df.index
# Index(['easy', 'executive', 'group'], dtype='object')
#df.columns
# Index(['journey_id', 'driver_id'], dtype='object')

       Сброс индекса
# df.reset_index  - перевести индекс датафрэйма в колонку. Индексом становится дефолтная последовательность чисел от 0 до N-1, где N – число строк.
# df.reset_index(drop = True) - drop отвечает за то, будет ли индекс переведён в колонку или же убран из таблицы:
#
       Поиск пустых значений
#df.isna() – это чудо-метод, с помощью которого можно быстро найти пропущенные значения в датафрэйме.
# Применив его, на выходе мы получаем датафрэйм той же размерности, где в каждой ячейке будет стоять True или False в зависимости от того, было ли значение пропущено.
#df.isna().sum() - В связке с ним можно использовать, например, метод sum, чтобы посмотреть на число NA в разных колонках.
#
   Графики
# import seaborn as sns  # работает поверх matplotlib
# import matplotlib.pyplot as plt # даже в пандосе есть методы визуализации, которые работают поверх matplotl
# plt.show() - для визуализации графиков в пайчарме (писать после графика)
# df.orders.plot('hist', bins = 15) - Самый простой способ визуализировать данные – вызвать метод plot у датафрэйма (или его колонки).
# 'hist' -гистограмма значений в колонке orders. bins – это число диапазонов (корзин или бакетов), на которые мы разделяем значения.
# Другой вариант записи: df.orders.plot.hist(bins = 15)
# sns.barplot(x = 'lovely_brand', y = 'user_id', data = brands_loyalty) # строим график барплот,указываем данные с которых мы хотим брать значения data = ,
# указываем колонку по Х и по У
# sns.boxplot(data = users_data, x = 'lovely_brand', y = 'loyality') # строим график барплот,указываем данные с которых мы хотим брать значения data = ,
# указываем колонку по Х и по У
# sns.displot(loyalty_df.loyalty_score, kde=False) # строим график дисплот, а в качестве аргумента передаем loyalty_df.loyalty_score - колонка loyalty_score  в дата фрейме loyalty_df
#  kde=False - убирает линию (видимо) kde(математическая апроксимация), которая в пайчарме у меня не была видна
#      matplotlib -Базовая библиотека для рисования графиков в Python. На ней построены более продвинутые и простые в использовании библиотеки типа seaborn. Через matplotlib можно нарисовать что угодно, но часто на это уходит слишком много строк кода, и её в основном используют для тонкой настройки графиков и их сохранения
#Изменить размер - В figure в figsize подаётся кортеж (как список, только в круглых скобках) с масштабом графика формата (ширина, высота)
# plt.figure(figsize = (9, 6)) - например
# plt.savefig('1.jpg') - сохранение картинки
#
# print('есть ли пропущенные значения?',user_data.isna().sum())  функции .isna() и isnull() заполнят значения на False или True, в зависимости от того пропущенное значение или нет, False и True в свою очередь соответственно равны 0 и 1, после чего применяем функцию sum, так мы сможем узнать количество пропущенных значений
# print('есть ли пропущенные значения?',user_data.isnull().sum())
# df['X'].ne(4).idxmax() - находит первый  результат наблюдения не равный 4

# query('success_number == @max_success_number') - @ заменяет f-строку, позволяет использовать переменную в аргументах методов

                        SCILBOX

        Чтение и запись файлов
csv #- comma-separated values - данные разделенные запятой
df = pd.read_csv('file.csv', # функция считывания внешнего файла формата csv (можно выбрать необходимый формат)
                 encoding='windows-1251',
                 sep = ';',
                 index_col='название_столбца',
                 parse_dates=['Date'],
                 dayfirst=True)
# 'file.csv' - путь к файлу,
# sep - разделитель sep(по умолчаниию ',')
# encoding – параметр в read_csv, отвечает за кодировку текста, которая может быть различной. Самая распространённая – utf
# index_col='название_столбца' - название столбца, который будет выступать как столбец индексов
# index_col=[0] - индекс столбца, который будет выступать как столбец индексов
# parse_dates – указывает, стоит ли воспринимать даты как даты (по умолчанию они воспринимаются пандасом как строки).
    # пример pd.read_csv(path, parse_dates=['some_date', 'another_date'])
    # Параметр с датами может принимать несколько значений:
    # True – пытается перевести в дату первую колонку
    # список колонок – parse_dates=['some_date', 'another_date']
    # пытается перевести в дату указанные в списке колонки и столбцы create_data, payment_data
    # будут обрабатываться как даты
# dayfirst=True  - первое значение в дате это день или нет - True/False
# df['Date'].dt.name - номер дня недели в соответствии с данными в колонке с датами
# df['Date'].dt.name() - название дня недели в соответствии с данными в колонке с датами
# df['Date'].dt.month - номер месяца в соответствии с данными в колонке с датами
# df['Date'].dt.month() - название месяца в соответствии с данными в колонке с датами

df.to_csv('result.csv', sep=';', index_label='название_столбца') # записываем файл в формате csv
# 'result.csv' - путь к файлу,
# sep - разделитель sep(по умолчаниию ',')
# index_label='название_столбца' - название столбца, который будет выступать как столбец индексов

df.read_excel('file.xlsx', # функция считывания внешнего файла формата xlsx (можно выбрать необходимый формат)
                 sheet_name = 'sheet2',
                 index_col='название_столбца',
                 parse_dates=['Date'],
                 dayfirst=False)
# 'file.csv' - путь к файлу,
# sheet_name - имя страницы файла эксель, с которого будет списываться данные в данный датафрейм

df.to_excel('result.csv', index_label='название_столбца') # записываем файл в формате csv
# 'result.csv' - путь к файлу,
# sep - разделитель sep(по умолчаниию ',')
# index_label='название_столбца' - название столбца, который будет выступать как столбец индексов
# sheet_name - имя страницы файла эксель, на которую будут записываться данные из данного датафрейма


df = pd.DataFrame([['Anna', 23, 3],
                   ['Sam', 36, 12],
                   ['Bill', 33, 10],
    ])
df.columns = ['name', 'age', 'exp']

loc - по ключам (по именам)
df.loc[3] или df.loc[[1, 4, 5], ['Age']] # - передаются имена индексов и названия колонок - эти имена должны существовать
iloc - по индексам (по порядку с 0)
df.iloc[[0, 1, 2]] или df.loc[0, [0,2]] # - передаются  именно индексы  по порядку в датафрейме и индексы колонок по порядку

df.iloc[1, 2] # выведет 12
df.iloc[1:3, 1] # выведет
#1  36
#2  33
df.iloc[:, 0] # выведет все имена в столбик
df['name'] # выведет столбец имён
df[['name', 'exp']] # выведет два этих столбца
df.index = df['name'] # поменяли нумерацию в столбце индексов на значения столбца name
df.loc['Bill', 'age'] # выведет 33
df.loc['Sam':'Bill', 'exp'] # выведет 12 и 10 - столбец exp от Sam до Bill включительно
df.loc[:, 'Имя_нового_столбца'] = list(range(1, df.shape[0] + 1)) # заполнение нового столбца нумерацией от 1 до
# последней строки по возрастанию
df.info() # выведет всю информацию по дата фрейму
df.describe() # выведет сводные характеристики
df['i'].dtype # выведет тип данных в Series
df['i'].astype('int64') # поменяет тип данных на целочиселнные в столбце
df.shape[0] # выведет количество строк
df.shape[1] # выведет количество столбцов
df.columns # выведет название столбцов (в виде пандас индекс - похожий на список)
df.columns[2] # выводить таким образом можно, но задавать новое значение не получится
df.index # выведет название строк (в виде пандас индекс - похожий на список)
df.sum(axis=1) # axis выбирает по столбцам или по строкам будем суммировать
df['цифры'].nlargest(3) # найдет 3 самых больших элемента

df.head() # выведет первые 5 строк
df.tail() # выведет последние 5 строк
pd.read_csv("extraversion.csv", encoding = "UTF-8")# загрузка файла csv в файл
pd.concat([df.iloc[:, :4], df.iloc[:, 4:]], axis=1) # соединение двух датафреймов в один(в данном случае диапазона)
# axis=1 указывает что соединение идёт по горизонтали
df.rename(columns=lambda x: x.replace(' ', '_')) # переименование названий колонн - замена пробелов на "_" во всём датафрейме
df.iloc[:, 4:].rename(columns=lambda x: x.replace(' ', '_')) # -//- в указанном диапазоне
df['i'].isin('да') # выведет датафрейм с True/False
df['i'].value_counts() # подсчет уникальных значений в столбце
                # СОЗДАНИЕ НОВЫХ СТОЛБЦОВ
df['total'] = df['w1'] + df['w2'] + df['w3']
df['total_gr'] = df['total'] * 1000
df['total_gr'].apply(np.log) # применит функцию np.log ко всему столбцу total_gr
df['avloss'] = df.loc[:, 'w1': 'w3'].apply(np.mean, axis=1) # создаем новый столбец - в указанном диапазоне применяем
# функцию mean по строкам т.к axis=1
f = lambda x: x.max() - x.min() # создали функцию нахождения разницы между максимальным и минимальным значением
df['wrange'] = df.loc[:, 'w1': 'w3'].apply(f, axis=1) # создаем новый столбец - в указанном диапазоне применяем
# функцию f по строкам т.к axis=1

                # УДАЛЕНИЕ СТОЛБЦОВ и СТРОК
df.drop(['B', 'C'], axis=1) # удалить столбцы
df.drop([0, 1], axis=0) # удалить строки по индексу
df.drop(columns=['B', 'C'])
df.drop([0, 1])
        # Для Мультииндекса
df.drop(index=('falcon', 'weight')) # удалить строки в мультииндексом датафрейме
df.drop(index='cow', columns='small') # удалить строку и колонку
df.drop(index='length', level=1) # удалить строку по индексу
                # Группировка и агрегация
df.groupby('i') # выведет объект groupby
list(df.groupby('i'))[0] # выведет первый элемент groupby - это пара: 1 -название группы(уникальное значение
# по которому произошло сгруппирированние из указанного столбца), 2 - сгруппирированный датасет из этой группы,
# по этопу значению)
df.groupby('i').agg('sum') # сложили показатели отдельно по каждой группе
df.groupby('i').agg(['min', 'max', 'mean', 'median', 'sum']) # вывели несколько показателей по сгруппирированным данным

df.pivot_table(index='client_id',columns='Gender', values='price', aggfunc='sum', margins=True, margins_name='Total')
# index='client_id' - колонка по которой будем группировать
# columns='Gender' - дополнительная колонка по которой будем группировать(необязательна)
# values='price'    - колонка по которой будем производить подсчёт
# aggfunc='sum')    - функция которую будем выполнять к нашей колонке
# margins=True      - добавляется колонка ИТОГО
# margins_name='Total' - назвали колонку ИТОГО - 'Total'

pd.crosstab(index=users['Geography'], columns=users['Gender']) # еще один вариант группировки
pd.crosstab(index=users['Geography'], columns=users['Gender'], normalize='all')
# normalize='all' - получаем не числовое а процентное соотношение, all- нормализация по всем колонкам и по всем строчкам
# normalize='index' - получаем процентное соотношение, index - нормализация по строчкам
# normalize='columns' - получаем процентное соотношение, columns - нормализация по колонкам

                #Сортировка
df.sort_values('i') # сортировка датафрейма по столбцу i  по возрастанию- не вносит изменение в исходный датафрейм
df.sort_values('i', inplace=True) # сортировка датафрейма по столбцу i   по возрастанию - вносит изменение в исходный датафрейм
df.sort_values(['i', 'y'], ascending=False) # сортировка датафрейма по столбцу i, а затем по столбцу У (по убыванию
# - ascending=False)
                #Работа с Nan
df.isnull() # выведет датафрейм с True/False - если ноль/пусто то True
df.isnull().sum() # найдем количество ноль/пусто в каждом столбце
df.fillna(0) # заменяет все Nan на 0
df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False) # убирает все нули и пустые значения - строки
# axis=1,0 - выбираем что будет удаляться строки или столбцы
# how='any'/'all' - выбирает удаляется если все элементы Nan или хотя бы один
# thresh=int - не удалять те строки, где есть хотя бы thresh значений отличные от Nan
# subset=['name', 'toy'] - в каких столбцах смотреть Nan
# inplace=True/False - вносятся ли изменения в исходный список

                #Иерархическое индексирование
df.set_index(['colum_1', 'colum_2'], inplace=True) # создаёт группирированный индекс - сначала по 'colum_1' затем по 'colum_2'
df.sort_index() # соортировка по индексам
df.loc['index_colum_1'] # выведет индексы 'column_2 и его значения по 'index_colum_1'
df.loc['index_colum_1', 'index_colum_2'] # выведет значения по индексам 'index_colum_2' соответствующих индексам 'index_colum_1'


df.iterrows() #- создаёт вместо каждой строки row=[], кортеж (index, row[])
df.itertuples() #- перебирает строки