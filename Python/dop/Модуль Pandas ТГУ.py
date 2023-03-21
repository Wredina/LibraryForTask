import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#           Посмотреть тип данных
# reviews.price.dtype - покажет типы данных конкретной колонки dtype('float64')
# reviews.dtypes - покажет типы данных всех колонок


# data = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']},
#                    index=['Product A', 'Product B']) # создание датафреймов со своими индексами
# titanic.iloc[0:3, 3] = "anonymous" # присвоение первым 3м элементам в третьем столбце значения 'anonymous'
# air_quality.reset_index(level=0) - reset_index(level=0) преобразование любого уровня индекса в столбец

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e']) #  np.random.randn(5) генерирует случайные 5 чисел, index - задаёт индексы
print(s) # выводит
# a   -1.192392
# b    1.049649
# c    1.081944
# d   -1.764988
# e    0.846093
# dtype: float64

s = pd.Series(range(3), index=pd.DatetimeIndex(['2020-01-01', '2020-01-02', '2020-01-03'])) # index=pd.DatetimeIndex([]) - задает в качестве индекса даты
print(s) # выводит
# 2020-01-01    0
# 2020-01-02    1
# 2020-01-03    2
# dtype: int64

print(s.index) # выведет DatetimeIndex(['2020-01-01', '2020-01-02', '2020-01-03'], dtype='datetime64[ns]', freq=None)


#       Сравнение Датафреймов

# Пример 1
df1 = pd.DataFrame({'x': [1, 3, 2], 'y': [2, 4, 1]})
df2 = pd.DataFrame({'x': [3, 1, 2], 'y': [0, 2, 2]})

print(df1 >= df2)
#        x      y
# 0  False   True
# 1   True   True
# 2   True  False

print ((df1 >= df2).any(axis=1))  # .any возвращает True, если есть хотя бы одна True в строке/столбце (axis=1 - столбец, axis=0 - строка)
# 0   True
# 1   True
# 2   True

print((df1 >= df2).all)  # возвращает True если все значения будут True в строке/столбце (axis=1 - столбец, axis=0 - строка)
# x   False
# y   False

# Пример 2
my_data = {'x': range(50), 'y': np.random.randn(50), 'z': np.random.randn(50)}
df = pd.DataFrame(my_data)
print(df.head()) # выведет
#    x         y         z
# 0  0  1.268261 -0.204649
# 1  1  1.860572  0.299567
# 2  2  0.734421 -1.798566
# 3  3 -1.222831  0.442688
# 4  4  0.610926 -0.498994

print(df[df >= 4]) # отфильтруем весь датафрейм что бы числа были >=4
print(df >= 4) # создаст датафрейм с булевыми значениями True или False
print((df >= 1).all(axis=1)) # создаст датафрейм с булевыми значениями True или False - если все значения будут True в строке/столбце (axis=1 - столбец, axis=0 - строка)
print((df >= 1).all(axis=0))
# x    False
# y    False
# z    False
# dtype: bool
print((df >= 1).any(axis=0))
# x    True
# y    True
# z    True
# dtype: bool
data2 = pd.DataFrame({'A': [1, 3, 2], 'B': [2, 4, 1]})

#               Работа с пустыми значениями NaN, 0 и т.д.
#pd.isnull() и pd.notnull() - проверяет пустоек ли значение ил инет
#pd.dropna() - удаление НаНов
#pd.fillna(value= ....)) # - заполнение НаНов константой

print(data2.isnull()) # - выводит булевой датафрейм если есть NaN то будет True, если нет, то False
print(data2.mean()) # - элементы NaN не будут учитываться, т.е например mean = (2 + NaN + 4) / 2
print(data2.apply(np.cumsum)) # - тоже обходятся NaN
data3 = data2.apply(np.cumsum)
print(data2.dropna()) # - удаление НаНов
print(data2.fillna(value= 5.5)) # - заполнение НаНов константой
# df['Cabin'] = df['Cabin'].fillna('unknown') - заменяет все NaN на значения 'unknown'
print(data2.ffill()) # - заполнение НаНов соседними значениями
print()
d = pd.DataFrame({'A': [1,2,2,1,2,3,2,1,3], 'B': [1,2,3,4,1,2,3,3,4]})
print(pd.crosstab(d['A'], d['B'])) # сравнивает два столбца, по вертикали - первый столбец, по горизонтали - второй столбец,
# цифры показывают - как часто значения одного столбца совпадают со значениями другого по позициям
#B  1  2  3  4
# A
# 1  1  0  1  1
# 2  1  1  2  0
# 3  0  1  0  1
print()
# print(pd.rolling_mean(a,2)) - выдает ошибку # можно сумму, медиану и любую функцию -
# сравнивает два столбца, по вертикали - первый столбец, по горизонтали - второй столбец,
# цифры показывают - функцию значения одного столбца со значениями другого по позициям
print(df.duplicated()) # покажет где есть дубликаты
# df.drop_duplicates(['name'], keep = 'first') # удалит дубликаты

#       Объединение датафреймов
left = pd.DataFrame({'key': [1,2,1], 'l': [1,2,3]})
right = pd.DataFrame({'key': [1,2,3], 'r': [4,5,6]})
# air_quality = pd.concat([air_quality_pm25, air_quality_no2], axis=0) # объединение двух датафреймов в один по строкам
# air_quality_ = pd.concat([air_quality_pm25, air_quality_no2], keys=["PM25", "NO2"]) # сортировка двух датафреймов в один по строкам, при этом сортируются по ключам keys=["PM25", "NO2"]
# air_quality = pd.merge(air_quality, stations_coord, how='left', on='location') # объединение двух датафреймов в один
#  Выбрав объединение left, в результирующей таблице air_quality окажутся только местоположения, доступные в (левой) таблице, например FR04014, BETR801 и London Westminster.
# air_quality = pd.merge(air_quality, air_quality_parameters, how='left', left_on='parameter', right_on='id') # в отличии от прошлой строки кода:
#  нет общего имени столбца. Однако столбец parameter в таблице air_quality и столбец id в air_quality_parameters содержат переменную в общем формате.
#  Аргументы left_on и right_on используются, чтобы сделать связь между двумя таблицами.
leftright = pd.merge(left, right, on='key') # объединение датафреймов  по ключам - ключи отсортировались по порядку - 1,1,2,
# ключа 3 нет в одном из датафреймов, под ключом 1 в 'l'- 1 в 'r'-4,  второй раз под ключом 1 в 'l'- 3 в 'r'нету поэтому берем опять 4,
# под ключом 2 в 'l'- 2 в 'r'- 5
print(leftright) # выведет
#    key  l  r
# 0    1  1  4
# 1    1  3  4
# 2    2  2  5

#       Фильтрация
# mask = titanic_df['Survived'] == 1 # выведет Серию с булевыми значениями где условие выполняется - True. где не выполняется = False
# mask = titanic_df['Age'] < 37 # выведет Серию с булевыми значениями где условие выполняется - True. где не выполняется = False
# titanic_df[mask] - выведет наш датафрейм удовлетворяющий условиям mask, т.е выведет только те ячейки, где в датафрейм mask было написано True
# titanic_df[titanic_df]

#       Сортировка
# titanic_df.sort_values('Name') - сортировка по имени - по колонке Name
# countries_reviewed.sort_values(by=['country', 'len']) - сортировка сначала по колонке country, а затем по колонке 'len'
# sorted_varieties = price_extremes.sort_values(by=['min', 'max'], ascending=False)  сортировка по двум переменным, ascending=False - в обратном порядке

# # 1) Первый вариант решения
# mask_female = titanic['Sex'] == 'female'
# mask_survivor = titanic['Survived'] == 1
# mask = mask_female & mask_survivor
# titanic[mask]
#
# # 2) Второй вариант решения
# titanic[(titanic['Sex'] == 'female') & (titanic['Survived'] == 1)]

# # 3) Третий способ решения
# females = titanic[titanic['Sex'] == 'female']
# female_survivors = females[females['Survived'] == 1]

# # 4) Четвертый способ решения - таблица по всем выжившим - мужчины и женщины
# titanic.groupby(['Sex', 'Survived'])['PassenserId'].count

# titanic.to_excel('titanic.xlsx', sheet_name='passengers', index=False) - сохраним данные в иксель

# По Заданию Кэгл

# 1
# bargain_idx = (reviews.points / reviews.price).idxmax() # находим отношение одной колонки к другой,
# # после чего применили функцию idxmax. которая возвращает индекс максимального значения в столбце.
# bargain_wine = reviews.loc[bargain_idx, 'title'] # возвращаем из столбца title позицию с id , которое мы нашли в переменной bargain_idx

# 2
# n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum() # description.map - перебирает все строки в столбце description
# а функция  lambda desc: "tropical" in desc - смотрит есть ли в каждой строке слово "tropical", а .sum() подсчитывает их количество
# n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum() - то же самое то со словом "fruity"
# descriptor_counts = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity']) # создаем серию где в индексе - наши искомые слова, а в столбце их количество

# 3.1

# def remean_points(row):                           # создаем функцию в которую подается аргумент(строка)
#     row.points = row.points - review_points_mean  # вычитаем из столбца points в нашей строке средний результат по этому же столбцу
#     return row    # возвращаем целую строку уже с новым результатов по столбцу points
#
# reviews.apply(remean_points, axis='columns') # добавляем наш результат в новый столбец нашего датафрейма

# 3.2

# def stars(row):                                        # создаем функцию в которую подается аргумент(строка)
#     if row.points >= 95 or row.country == 'Canada':    # фильтруем строку по колонкам points и country, если страна Канада, то даём 3  и если points >= 95
#         return 3
#     elif row.points >= 85 :                            # если points >= 85 то даем 2 звезды, в остальных случаях 1 звезду
#         return 2
#     else:
#         return 1
#
# star_ratings = reviews.apply(stars, axis='columns')   # создаем серию в которую добавляем результаты нашей функции

# 4

# reviews.groupby('winery').apply(lambda df: df.title.iloc[0]) - группируем по колонке 'winery', и добавляем из колонки 'title' [0] элемент
# reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()]) группируем по двум колонкам ['country', 'province'],
# добавляем  элементы которые имеют наибольшие оценки в колонке points

# 5

#price_extremes = reviews.groupby(['variety']).price.agg([min, max]) - группируем по столбцу 'variety', далее выбираем
# столбец с ценами 'price' и применяем к ней две функции [min, max]

# 6

# country_variety_counts = reviews.groupby(['country', 'variety']).size().sort_values(ascending=False) - группируем по столбцам 'country', 'variety'
# затем size() смотрит видимо количество, затем сортируем в обратном порядке - ascending=False



            # Лекция Извлечение и группировка
#               pandas-profiling - библиотека
# !pip3 install pandas-profiling==2.11 - обновляет версию pandas-profiling, если pip то так, если anaconda, то скорее всего нужно писать conda
# from pandas_profiling import ProfileReport - импортируем библиотеку
# profile = ProfileReport(example_df, title='Pandas Profiling Report')   - Составление отчета в ProfileReport
# коэффициенты Pearcon's r и Spearman's p позволяют определить направление корреляции (коэф. Phik не может этого делать), т.е
# 1 - это когда первая переменная растет. вторая тоже растет
# -1 - это когда первая переменная растет, вторая уменьшается

# Заливка файлов в коллабе (на текущий момент не работает):
# from google.colab import files
# uploaded = files.upload()

#                                                   Нахождение минимума в группах

d = pd.DataFrame({'A': [1,2,2,1,3,3],
                  'B': [1,2,3,3,2,1]})
print(d) # выведет
#    A  B
# 0  1  1
# 1  2  2
# 2  2  3
# 3  1  3
# 4  3  2
# 5  3  1

# 1) Первый способ
print(d.loc[d.groupby('A')['B'].idxmin()]) # находим id минимума - мы сгруппировали по колонке А и вывели id минимума по колонке B , выведет
# т.е. у нас получилось по колонке А и у нас получилось три группы (1=1-1 и 1-3, 2= 2-2 и 2-3, 3=3-2 и 3-1) и вывели минимум из них по колонке  В
#    A  B
# 0  1  1
# 1  2  2
# 5  3  1

# 2) Второй способ

print(d.sort_values('B').groupby('A', as_index=False).first()) # выведет тоже самое

# Вывод всех групп
a = pd.DataFrame({'A': [1,2,2,1,1,2,2],
                  'B': [3,4,3,4,3,3,4],
                  'C': [5,5,5,6,6,6,6]}) # по группировке ['A', 'B'] всего получается 4 группы - (1, 3), (1, 4), (2, 3), (2, 4)
print(a.groupby(['A', 'B']).groups) # выведет {(1, 3): [0, 4], (1, 4): [3], (2, 3): [2, 5], (2, 4): [1, 6]} -
# (2, 4)- это пара цифр по группировке ['A', 'B'] , а : [0, 4] - это индексы, на которых эти пары встречаются
for x, y in a.groupby(['A', 'B']):
    print(x)
    print(y)
# Выведет:
# (1, 3) - наша текущая группа
#    A  B  C - название столбцов
# 0  1  3  5 - строка значений по первому индексу где встречается наша группа
# 4  1  3  6 - строка значений по второму индексу где встречается наша группа
# (1, 4)
#    A  B  C
# 3  1  4  6
# (2, 3)
#    A  B  C
# 2  2  3  5
# 5  2  3  6
# (2, 4)
#    A  B  C
# 1  2  4  5
# 6  2  4  6

print(a.groupby(['A', 'B']).first()) # группируем по ['A', 'B'] и при этом по первому элементу, выведет:
# A B
# 1 3  5   - группировка по первому элементу, т.е по колонке А, там только 2 группы - 1 и 2, в группе 1 только две подгруппы - 1-3 и 1-4
#   4  6
# 2 3  5  - в группе 1 только две подгруппы - 2-3 и 2-4
#   4  5

print(a.groupby(['A', 'B'])['C'].mean()) # средние по группам, выведет
# A  B
# 1  3    5.5
#    4    6.0
# 2  3    5.5
#    4    5.5
# Name: C, dtype: float64

print(a.groupby(['A', 'B']).get_group((1,3))) # выбор конкретной группы, выведет:
#    A  B  C
# 0  1  3  5
# 4  1  3  6
print(a.groupby(['A', 'B']).cumcount()) # - номер в группе, можно группировать по столбцам...

# Пример - сколько людей в каком порту село
# embarked_totals = df.groupby('Embarked')['PassengerId'].count() - группируем по портам ('Embarked') и по ['PassengerId'].count() - считаем количество

# Пример - выживших по тем в каком порту сели
# survived_totals = df.groupby('Embarked')['Survived'].sum() - группируем по портам ('Embarked') и по ['Survived'].sum()
# - считаем сумму(выжившие это 1, не выжившие учитываться не будут, т.к. это  0)
# suvived_totals / embarked_totals * 100 - отношение выживших от всех пассажиров
# df.groupby('Embarked').get_group('S') - получение групп именно по людям вошедшим в порту S

# Пример - группировка по полу и выживаемости и подсчет среднего возраста
# df.groupby(['Survived', 'Sex'])['Age'].agg(np.median) - выведет в столбик группу по Survived затем подгруппу по Sex  и далее столбик со средними значениями

# Пример - более сложный пример

# df.groupby(['Survived', 'Sex', 'Pclass']).agg({'Age': np.median, 'Fare': np.mean, 'PassengerId': len}) -
# выведет в столбик группу по Survived затем подгруппу по Sex и подподгруппу Pclass и далее столбики  в каждой подподгруппе
# с медианными значениями по возрасту, средними по стоимости проезда и с количеством пассажиров

# print(a.groupby(['A', 'B'])['C'].agg({'sum': np.sum, 'mean': np.mean})) # агрегация по одному столбцу - что то не работает)
# titanic.agg({'Age': ['min', 'max', 'median', 'skew'], 'Fare': ['min', 'max', 'median', 'mean']}) - пример агрегации по двум столбцам и нескольким функциям, выведет:
#           Age	           Fare
# max	    80.000000	512.329200
# mean	    NaN	        32.204208
# median	28.000000	14.454200
# min	    0.420000	0.000000
# skew	    0.389108	NaN

# Пример отклонение температуры пациента от обычной в определенной подгруппе
mmean = lambda  x: (x-np.mean(x)) # для каждого значения считаем разницу - значение минус среднее по этой группе, здесь Х - это вся серия, весь столбец
print(a.groupby('A').transform(mmean)) # трансформация по группам в которых вычли среднее
# выведет
#           B         C
# 0 -0.333333 -0.666667
# 1  0.500000 -0.500000
# 2 -0.500000 -0.500000
# 3  0.666667  0.333333
# 4 -0.333333  0.333333
# 5 -0.500000  0.500000
# 6  0.500000  0.500000

#                                   Фильтрация групп
print(a.groupby('A').filter(lambda  x: x['B'].sum()>10, dropna=False)) # фильтрация по группам, т.е выбор групп которые соответствуют требованиям
# groupby('A') - группирует по столбцу А, получаются группы 1 и 2,
# filter(lambda  x: x['B'].sum()>10, dropna=False)) - выводит только те группы у которых сумма всех значений B > 10
# Выведет
#      A    B    C
# 0  NaN  NaN  NaN
# 1  2.0  4.0  5.0
# 2  2.0  3.0  5.0
# 3  NaN  NaN  NaN
# 4  NaN  NaN  NaN
# 5  2.0  3.0  6.0
# 6  2.0  4.0  6.0

#                                    Применение функций

# pipe() - Применяется к датафрему целиком
# apply() - к строкам/столбцам
# applymap() - поэлементно

# Применение pipe()

pipe_example_df = pd.DataFrame({'A': [1, 1, 1, 2, 2, 2], 'B': [1, 2, 3, 1, 2, 3], 'C': [1, 2, 1, 2, 1, 2]})

def make_copy(dataframe):   # функция которая создает копию датафрейма
    return dataframe.copy()

def add_total(dataframe):   # функция которая складывает копию в один датафрейм
    dataframe['Total'] = dataframe['A'] + dataframe['B'] + dataframe['C']
    return dataframe

print(add_total(make_copy(pipe_example_df))) # берем датафрейм pipe_example_df применяем к нему операцию make_copy, а потом к результату применяем операцию add_total
# выведет
#    A  B  C  Total
# 0  1  1  1      3
# 1  1  2  2      5
# 2  1  3  1      5
# 3  2  1  2      5
# 4  2  2  1      5
# 5  2  3  2      7

print(pipe_example_df.pipe(make_copy).pipe(add_total))  # берем датафрейм pipe_example_df применяем к нему операцию make_copy, а потом к результату применяем операцию add_total
# Выведет тоже самое
#    A  B  C  Total
# 0  1  1  1      3
# 1  1  2  2      5
# 2  1  3  1      5
# 3  2  1  2      5
# 4  2  2  1      5
# 5  2  3  2      7
print()
# print((pipe_example_df - другой вариант написания дополнительные скобки дают возможность переносить каждую функцию на новую строку
#        .pipe(make_copy)
#        .pipe(add_total)))

# Применение apply()
# Пример 1
def f(x): # функция - вычесть среднее от значения
    return pd.DataFrame({'x': x, 'x-mean': x - x.mean()})
print(a.groupby('A')['B'].apply(f)) # - сгруппировали по значениям столбца А, и к столбцу В применили нашу функцию - вычесть среднее ко всем элементам столбца
# выведет
#    x    x-mean
# 0  3 -0.333333
# 1  4  0.500000
# 2  3 -0.500000
# 3  4  0.666667
# 4  3 -0.333333
# 5  3 -0.500000
# 6  4  0.500000

# Пример 2
print(a.apply((lambda x: x/sum(x)))) # apply берет анонимную функцию лямбда и применяет её по всем столбцам
# выведет
#           A         B         C
# 0  0.090909  0.125000  0.128205
# 1  0.181818  0.166667  0.128205
# 2  0.181818  0.125000  0.128205
# 3  0.090909  0.166667  0.153846
# 4  0.090909  0.125000  0.153846
# 5  0.181818  0.125000  0.153846
# 6  0.181818  0.166667  0.153846

# print(a.apply((lambda x: x/sum(x), axis=1))) # apply берет анонимную функцию лямбда и применяет её по всем строкам - ЧТО ТО НЕРАБОТАЕТ

# Применение applymap()
a = pd.DataFrame({'A': [1,2,2], 'B': ['a','b','a']})

def some_fn(x):
    if type(x) is str: # если х число то умножаем на 10, а если строка, то пишем 'applymap_' + x
        return 'applymap_' + x
    else:
        return (10*x)

print(a.applymap(some_fn)) # применит функцию к каждому элементу нашего датафрейма
# выведет
#     A           B
# 0  10  applymap_a
# 1  20  applymap_b
# 2  20  applymap_a

#           Применение функции map()

# Пример 1
d = pd.DataFrame({'A': [1,2,2,1,2,3,2,1,3], 'B': ['as', 'bs', 'e', 'qq', 'aaa', 'a', 'e', 'qwr', 'www']})
print(d[d['B'].map(lambda  x: x.startswith('a'))]) # map применяет к каждому элементу какую то функцию
# выведет
#    A    B
# 0  1   as
# 4  2  aaa
# 5  3    a
# Пример 2
df = pd.DataFrame({'name': ['Маша', 'Саша', 'Рудольф'], 'marks': [[2,3,3,5], [4,5,5], [2,3]]})
print(df[df['marks'].map(lambda  x: 3 in x)]) # map применяет к каждому элементу какую то функцию
# выведет
#       name         marks
# 0     Маша  [2, 3, 3, 5]
# 2  Рудольф        [2, 3]

# Пример 3
df = pd.DataFrame({'CITY': ['London', 'Moscow', 'Paris'], 'Stats': [0,2,1]})

d = {'London':'GB', 'Moscow':'RUS', 'Paris': 'FR'}
df['country'] = df['CITY'].map(d) # добвляет в новый столбик country значения в соответствии с датафреймом d
df.columns = map(str.lower, df.columns) # делает названия столбцов с маленькой буквы
print(df)
# выведет
#      city  stats country
# 0  London      0      GB
# 1  Moscow      2     RUS
# 2   Paris      1      FR


#    Сводные таблицы                       Pivot

p_df = pd.DataFrame({
    'region': ['US', 'UK', 'UK', 'US', 'US', 'UK', 'US', 'US', 'UK', 'UK'],
    'store': [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],
    'article': ['cheeseburger',
                'coffee',
                'cheeseburger',
                'coffee',
                'cheeseburger',
                'coffee',
                'cheeseburger',
                'coffee',
                'cheeseburger',
                'coffee',],
    'amount': [1, 2, 3, 4, 5, 2, 3, 4, 5, 6],
}, index=pd.date_range(start='2021-01-01', periods=10))
print(p_df) # выведет
#            region  store       article  amount
# 2021-01-01     US      1  cheeseburger       1
# 2021-01-02     UK      1        coffee       2
# 2021-01-03     UK      1  cheeseburger       3
# 2021-01-04     US      1        coffee       4
# 2021-01-05     US      1  cheeseburger       5
# 2021-01-06     UK      2        coffee       2
# 2021-01-07     US      2  cheeseburger       3
# 2021-01-08     US      2        coffee       4
# 2021-01-09     UK      2  cheeseburger       5
# 2021-01-10     UK      2        coffee       6

pivoted_df = p_df.pivot_table(values='amount', index=['region', 'store'], columns='article', aggfunc='sum')
print(pivoted_df) # выведет
# article       cheeseburger  coffee
# region store
# UK     1                 3       2
#        2                 5       8
# US     1                 6       4
#        2                 3       4

# сводная таблица берет какую то категорию, для каждого уникального товара в этой категории заводит свой столбик,
# а в строки делает то почему мы группировали в данном случае region и store, а в значениях будут, значения из столбца amount
#values='amount', - значения будут из столбца amount
# index=['region', 'store'],  - индексы будут region и второй индекс store
# columns='article',  - столбцы будут значения из колонки article
# aggfunc='sum' - функция применяемая к нашим ячейкам - сумма

print(pd.melt(pivoted_df.reset_index(), id_vars=['region', 'store'])) # melt - это обратная операция

#       Упражнение из видео
# df = pd.read_csv('titanic.csv', encoding='windows-1251', sep = '\t', index_col='PassengerId')
# def split_name(name):
#     last_name, rest = name.split(', ')  - разбиваем значение по запятым с пробелом - получается два элемента - фамилия и остаток
#     title, rest = rest.split('.') - разбиваем то что получилось на '.' и задаем на два элемента
#     return title - выводим из этих двух элементов нужный
# df['Title'] = df['Name'].apply(split_name) - применяем нашу функцию ко всему столбцу Name
# df.Title.unique() # выведет array(['Mr', 'Mrs', 'Miss', 'Master', 'Don', 'Rev'], dtype=object)

#                                               Лекция 6

#                   Категориальные переменные
# создание категориального признака = интервалы попаданий
x = np.random.randn(10000) # создает 10000 случайных чисел
print('X')
print(x)
y = pd.cut(x,10) # делим наши числа на 10 категорий
print()
print('Y')
print(y)
z = pd.value_counts(y) # задаем значения для датафрейма Z по которому будем строить первый график
z.plot(figsize=(20,3)) # строим первый график по значениям датафрейма Z
pd.DataFrame(x).plot(kind='kde') # строим график второй график по значениям датафрейма Х
pd.DataFrame(z).T # = .T - транспонирование матрицы - т.е столбцы становятся строками и наоборот
plt.show()
#       несколько столбцов из одного:
a = pd.DataFrame({'d':[1,2,1,2],'b':[3,3,3,4]})
print(a)
def two_three_strings(x):
  return x*2, x*3
print('a["d"]')
print(a['d']) # это серия
a['twice'], a['thrice'] = zip(*a['d'].map(two_three_strings))
print('a')
print(a)
print("*a['d']")
print(*a['d']) # без принта * не работает как распаковщик
print(a['d'].map(two_three_strings)) # каждый наш элемент 1 2 1 2 прогнали через функцию two_three_strings
# и получается каждый элемент умножили на 2 и на 3 - (1*2=2, 1*3=3) (2*2=4, 2*3=6) (1*2=2, 1*3=3) (2*2=4, 2*3=6)
# выведет
# 0    (2, 3)
# 1    (4, 6)
# 2    (2, 3)
# 3    (4, 6)
# Name: d, dtype: object
print(zip(*a['d'].map(two_three_strings))) # выведет <zip object at 0x000002C197D166C0>
print(list(zip(*a['d'].map(two_three_strings)))) # выведет [(2, 4, 2, 4), (3, 6, 3, 6)]
# пример в примере
x = [1,2,3]
y = [4,5,6]
print(list(zip(x,y))) # выведет [(1, 4), (2, 5), (3, 6)],  т.е zip соединил в кортежи по индексам элементы из первого и второго списка в один

#           Один столбец на основе нескольких
a['total'] = a['d'] + a['b'] + a['twice'] + a['thrice'] # можно умножать, складывать, делить , вычитать и т.д
print(a) # выведет
#    d  b  twice  thrice  total
# 0  1  3      2       3      9
# 1  2  3      4       6     15
# 2  1  3      2       3      9
# 3  2  4      4       6     16

# одна колонка из нескольких str содержания
df = pd.DataFrame({'name': ['Маша', 'Саша', 'Рудольф'], 'surname': ['Петрова', 'Сидоров', 'Кац']}) # из имени и фамилии делаем полное имя
# первый способ
lst = []
for n, s in zip(df.name, df.surname):
    lst.append(n + ' ' + s)
df['fullname'] = lst
# второй способ
df['fullname2'] = df[['name', 'surname']].apply(lambda x: x[0] + ' ' + x[1], axis=1)
# третий способ
df['fullname3'] = df['name'] + ' ' + df['surname']
print(df)
# выведет
#       name  surname      fullname     fullname2     fullname3
# 0     Маша  Петрова  Маша Петрова  Маша Петрова  Маша Петрова
# 1     Саша  Сидоров  Саша Сидоров  Саша Сидоров  Саша Сидоров
# 2  Рудольф      Кац   Рудольф Кац   Рудольф Кац   Рудольф Кац


#                                     Временные ряды
#временные ряды
data ={'date':['2014-05-01 18:47:05.069722', '2014-05-01 18:47:05.119994', '2014-05-02 18:47:05.178768', '2014-05-02 18:47:05.230071', '2014-05-02 18:47:05.230071', '2014-05-02 18:47:05.280592', '2014-05-03 18:47:05.332662', '2014-05-03 18:47:05.385109', '2014-05-04 18:47:05.436523', '2014-05-04 18:47:05.486877'],
       'battle_deaths':[34,25,26,15,15,14,26,25,62,41]} # словарь с ключом date и ключом battle_deaths

df = pd.DataFrame(data) # сохраняем словарь data в новую переменную как датафрейм
df.index = pd.to_datetime(df['date']) # в качестве index копируем колонку date
del df['date'] # удаляем колонку date
print(df) # распечатает получившийся датафрейм
# print(df['5/1/2014']) # распечатает все строки по определенной дате  # df['2014-05-01'] - устаревший способ пайчарм ругается
print(df.loc['5/1/2014']) # распечатает все строки по определенной дате  # df['2014-05-01']
# Переход к дням и визуализация
print()
print(df.resample('D').mean().plot(kind='bar')) # выведет AxesSubplot(0.125,0.11;0.775x0.77)
df.resample('D').mean() # resample это команда группировки по диапазону данных
plt.show()

#                   Задание типов данных для колонок
# sunspots_df = pd.read_csv('sunspots.csv') - загрузка файла
# sunspots_df.head() # выведет
# Unnamed: 0	Date	Monthly Mean Total Sunspot Number               изначально каждая колонка это str
# 0	0	    1749-01-31	                            96.7
# 1	1	    1749-02-28	                            104.3
# 2	2   	1749-03-31	                            116.7
# 3	3	    1749-04-30	                            92.8
# 4	4	    1749-05-31                      	    141.7

# sunspots_df = sunspots_df.astype({'Date': 'datetime64', 'Monthly Mean Total Sunspot Number': 'float'}) # .astype - задаем тип даных нашим колонкам ({'название колонки': 'тип данных',...})
# sunspots_df.info() # выведет
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 3235 entries, 0 to 3234
# Data columns (total 3 columns):
#  #   Column                             Non-Null Count  Dtype
# ---  ------                             --------------  -----
#  0   Unnamed: 0                         3235 non-null   int64
#  1   Date                               3235 non-null   datetime64[ns]
#  2   Monthly Mean Total Sunspot Number  3235 non-null   float64
# dtypes: datetime64[ns](1), float64(1), int64(1)
# memory usage: 75.9 KB                                   т.е в строках три колонки, в столбце Dtype указан тип данных

# Индексация
# sunspots_df.index = pd.to_datetime(sunspots_df['Date']) # устанавливаем в индекс колонку Date и преобразуем их значения в даты
# del sunspots_df['Date'] # удаляем колонку Date
# del sunspots_df['Unnamed: 0']  # удаляем колонку Unnamed: 0
# sunspots_df # выведет
# 	        Monthly Mean Total Sunspot      Number
# Date
# 1749-01-31	                            96.7
# 1749-02-28	                            104.3
# 1749-03-31	                            116.7
# 1749-04-30	                            92.8
# 1749-05-31	                            141.7

# sunsports_df.plot()  выведет график вспышек на солнце
# sunspots_df['2000':'2010'].resample('1Y').mean().plot() - ['2000':'2010'] - диапазон временной, resample('1Y') - группировка и внутри частотность графика


#               Строки
# Регулярные выражения - regex101.com, regexr.com
s =pd.Series(['AbA','Sasha','DataMining'])
s = s.str.lower()
print(s) # выведет
# 0           aba
# 1         sasha
# 2    datamining
# dtype: object
print(s.str.contains('aba')) # проверяет есть ли 'AbA' в датафрейме s (можно проверить только в столбце) выведет
# 0    True
# 1    False
# 2    False
# dtype: bool

#           Скользящие
#           - rollinf(5) можно применять sum, mean, max, min  и т.д
#           - expanding(12).mean() расширяющуюся среднее - т.е берет не все время между двумя соседними а сначала 1 индекс, потом 2 индекса, потом 3 индекса , потом 4 и т.д
a = pd.DataFrame({'x':[1,2,3,1,2,3,1,2,3], 'y':[2,2,10,2,2,2,2,2,2]})
print(a.rolling(2).mean()) #  rooling(2).mean() - это средние значения между 2 соседствующими значениями .....выведет
#      x    y
# 0  NaN  NaN
# 1  1.5  2.0
# 2  2.5  6.0
# 3  2.0  6.0
# 4  1.5  2.0
# 5  2.5  2.0
# 6  2.0  2.0
# 7  1.5  2.0
# 8  2.5  2.0

#           Корреляция
s1 = pd.Series(np.cos(np.arange(100))) # создаем серию по косинусу
s2 = pd.Series(np.sin(np.arange(100))) # создаем серию по синусу
f = pd.DataFrame({'s1':s1,'s2':s2}).plot() # создаем датафрейм с предыдущими сериями
s1.rolling(5).corr(s2).plot(style='.') # скользящая корреляция) и график к ней)
f.legend(['signal 1','signal 2','corr']) # прописываем легенду к нашему графику
plt.show()

#           Кумулятивные функции
s1 = pd.Series(np.cos(np.arange(100))) # создаем серию по косинусу
s2 = s1.expanding().mean() # создаем серию с расширяющимися средними
f = pd.DataFrame({'s1':s1,'s2':s2}).plot()  # создаем датафрейм с предыдущими сериями
f.legend(['signal','cum_mean']) # прописываем легенду к нашему графику
plt.show()

#           Удаление дубликатов
df =pd.DataFrame({'name':['Al','Max','Al'], 'surname':['Run1','Crone','Run2']})
#   name surname
# 0   Al    Run1
# 1  Max   Crone
# 2   Al    Run2
print(df.duplicated()) # выведет
# 0    False
# 1    False
# 2    False
# dtype: bool
df = df.drop_duplicates(['name'], keep='first') # drop_duplicates - удаление дубликатов, ['name'] - по каким столбцам мы смотрим дубликаты и keep='first' - оставляем первый столбец из дубликатов
print(df) # выведет
#   name surname
# 0   Al    Run1
# 1  Max   Crone


#                   Максимальный элемент
m_df = pd.DataFrame({'date': pd.date_range('2020-01-01', periods=8), 'store': [1, 1, 1, 1, 2, 2, 2, 2], 'article': [1, 2, 3, 1, 2, 3, 1, 2], 'amount': [12, 22, 11, 77, 45, 4, 1, 2]})
print(m_df) # выведет
#         date  store  article  amount
# 0 2020-01-01      1        1      12
# 1 2020-01-02      1        2      22
# 2 2020-01-03      1        3      11
# 3 2020-01-04      1        1      77
# 4 2020-01-05      2        2      45
# 5 2020-01-06      2        3       4
# 6 2020-01-07      2        1       1
# 7 2020-01-08      2        2       2
#
# Process finished with exit code 0

print(m_df.groupby(['store', 'article'])['amount'].max()) # группируем по ['store', 'article'], затем по колонке 'amount' смотрим максимальные значения в этих группах
# выведет
# store  article
# 1      1          77
#        2          22
#        3          11
# 2      1           1
#        2          45
#        3           4
# Name: amount, dtype: int64

print(m_df['amount'].idxmax())  # индекс самого большого элемента = 3

# Несколько самых больших элементов
print(m_df.amount.nsmallest(3)) # выводит 3 самых маленьких элемента в серии
# 6    1
# 7    2
# 5    4
# Name: amount, dtype: int64
print(m_df.amount.nlargest(2)) # выводит 2 самых больших элемента в серии
# 3    77
# 4    45
# Name: amount, dtype: int64
print(pd.value_counts([3, 2, 2, 2, 5, 3],sort=False)) # сколько каждого значения # выведет
# 3    2
# 2    3
# 5    1
# dtype: int64
print(pd.DataFrame({'x':[3, 2, 2, 2, 5, 3, 3]}).mode()) # мода # выведет
#    x
# 0  2
# 1  3

#                   Кодирование категориальных переменных
# делает значение категорий равноудаленными друг от друга
print(pd.get_dummies([1,2,1,2,3])) # выведет
#    1  2  3
# 0  1  0  0
# 1  0  1  0
# 2  1  0  0
# 3  0  1  0
# 4  0  0  1
print(pd.Series(['one,two', 'two,three', 'one!']).str.get_dummies(sep=',')) # выведет
#    one  one!  three  two
# 0    1     0      0    1
# 1    0     0      1    1
# 2    0     1      0    0

#       Порядковое кодирование
#       - если данные являются шкалой, но при этом они не совсем одномерные, применяются следующие функции
print(pd.factorize([20,10,np.nan,10,np.nan,30,20]))
# выведет (array([ 0,  1, -1,  1, -1,  2,  0], dtype=int64), array([20., 10., 30.])) # (-1) это и есть наши np.nan

#Чтобы преобразовать типы данных в pandas, есть три основных способа:
#         1) Используйте метод astype(), чтобы принудительно задать тип данных.
# df.astype({'Customer Number': 'int', 'Customer Name': 'str'}).dtypes -`astype()` может принимать словарь имен столбцов и типов данных:

#         2)Создайте настраиваемую (custom) функцию для преобразования данных.
#   1 способ
# def convert_currency(val):
#     new_val = val.replace(',', '').replace('$', '')
#     return float(new_val)
# df['2016'].apply(convert_currency)
#   2 способ
# df['2016'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')
# df['Percent Growth'].apply(lambda x: x.replace('%', '')).astype('float') / 100
#         3)Используйте функции to_numeric() или to_datetime().
# -
# pd.to_numeric(df['Jan Units'], errors='coerce') - обрабатывает числовые значения в float64,
# аргумент errors=coerce преобразует недопустимое значение, такие как Closed на значение NaN
# Мы можем оставить эти значения или заменить их на 0 с помощью fillna(0): pd.to_numeric(df['Jan Units'], errors='coerce').fillna(0)
# -
# pd.to_datetime(df[['Month', 'Day', 'Year']]) преобразует соответствующие колонки в месяц, день и год и объединяет в новую серию типа datateime64.

#                       np.where()
# df["Active"] = np.where(df["Active"] == "Y", True, False)   всем значениям 'Y' присваивается значение True а остальным значениям присваивается False


#                           Способ 2 Преобразования данных
# Если у вас есть файл с данными, который вы собираетесь обрабатывать повторно, и он всегда имеет один и тот же формат,
# вы можете задать параметры dtype и converters, которые будут применяться при чтении данных.
# dtype будет использоваться как astype(). Аргументы converters позволяют применять функции к различным входным столбцам.
# Вы можете применить dtype или функцию converter к указанному столбцу только один раз. Если вы попытаетесь применить оба к одному столбцу, то dtype будет пропущен.

# df_2 = pd.read_csv("https://github.com/dm-fedorov/pandas_basic/blob/master/%D0%B1%D1%8B%D1%81%D1%82%D1%80%D0%BE%D0%B5%20%D0%B2%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20pandas/data/sales_data_types.csv?raw=True",
#                    dtype={'Customer Number': 'int'},  # при чтении файла сразу используем dtype={} как astype()
#                    converters={'2016': convert_currency,  # используем converters={} в ключи задаем столбец, а в значение функцию для преобразования,
#                                                             в данном случае это наша написанная функция def convert_currency()
#                                '2017': convert_currency,  # в данном случае это наша написанная функция def convert_currency()
#                                'Percent Growth': convert_percent, #   в данном случае это наша написанная функция def convert_percent()
#                                'Jan Units': lambda x: pd.to_numeric(x, errors='coerce'), #  в данном случае это lambda функция преобразования во флоат функцию
#                                'Active': lambda x: np.where(x == "Y", True, False)}) # в данном случае это lambda функция преобразования в булевые значения


#           Переименовать
# reviews.rename(columns={'points': 'score'})                                           переименовали колонку 'points' в 'score'
# reviews.rename(index={0: 'firstEntry', 1: 'secondEntry'})                             переименовали первые пару строк
# reviews.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns')       переименовали оси вместо rows и columns  - wines и fields
#           Соединение
# left = canadian_youtube.set_index(['title', 'trending_date']) # сделали датафрейм где индексами выступают колонки 'title', 'trending_date'
# right = british_youtube.set_index(['title', 'trending_date']) # сделали датафрейм где индексами выступают колонки 'title', 'trending_date'
# left.join(right, lsuffix='_CAN', rsuffix='_UK') # соединили датафрейм right к датафрему left, где индексы всё те же общие колонки,
# а далее идут сначала колонки из датафрейма left и к названиям колонок прибавляется суфикс '_CAN', затем правые и к названиям колонок прибавляется суфикс '_UK'


words = lambda x: ' '.join([stemmer_r.stem(word) if ord(word[0]) > 1000 else stemmer_e.stem(word) for word in word_tokenize(x)])
#           Замена значений в датафрейме
df_onlain_msk .loc[(df_onlain_msk.schedule_name != 'Удаленная работа'), 'schedule_name'] = 'Работа в офисе (Junior)'
# df_onlain_msk - название датафрейма
# (df_onlain_msk.schedule_name != 'Удаленная работа') - прописанное условие
# 'schedule_name' - колонка по которой будем прогонять условие
# 'Работа в офисе (Junior)' - значение на которое заменяем
# 1 способ
# DataFrame.loc[condition, (column_1, column_2)] = new_value
# 2 способ
# DataFrame['column_name'] = numpy.where(condition, new_value, DataFrame.column_name)
# 3 способ
# DataFrame['column_name'].where(~(condition), other=new_value, inplace=True)
# Источник: https://tonais.ru/library/zamena-odnogo-ili-neskolkih-znacheniy-v-stolbtse-v-dataframe

#           Удаление строк по условию
# lambda, if и else


# np.max([0, 1, 12, 1, -9]) - выведет 12
# np.argmax([0, 1, 12, 1, -9]) - выведет 2,  - т.е индекс 12