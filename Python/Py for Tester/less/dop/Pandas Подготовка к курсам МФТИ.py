import numpy as np
import pandas as pd

pd.set_option('display.max_columns', None) # убирает ограничение вывода количества столбцов на экран
# pd.set_option('display.max_rows', None)    # убирает ограничение вывода количества строк на экран
pd.set_option('display.width', None)

# Создание
#  тип данных pd.Series представляет собой одномерный набор данных. Отсутствующие данные записываются как np.nan
#  они не участвуют в вычислении средних, среднеквадратичных отклонений и т.д

some_list = [1, 3, 5, np.nan, 6, 8] # тип данных будет float64, т.к np.nan имеет тип float64,
# а Серии умеют работать только с данными одного типа, поэтому он все данные приводит к одному типу
ser_1 = pd.Series(some_list)
print(ser_1)
print()

# Свои Индексы - Можно в явном виде указать индексы, чтобы потом было более удобно обращаться к элементам
# Имя Датафрейма - можно задать имя нашему датафрейму
ind = ['1st day', '2nd day', '3rd day', '4th day', '5rd day', '6th day'] # записали будущий индекс
ser_2 = pd.Series(some_list, index=ind, name='Temperature') # присвоили индексу список ind
print(ser_2)
print(ser_2['3rd day'])
print()

# Индексирование
# Можно работать так же как и с обычным листом
print('Индексы и срезы')
print(ser_2[0])
print()
print(ser_2[1:3])
print()
print(ser_2[:: -1])
print()

# Индексироваться можно по условиям
date_range = pd.date_range('20190101', periods=10) # создали диапазон дат
ser_3 = pd.Series(np.random.rand(10), date_range) #  мы сделали индексом наш диапазон дат, второй аргумент  date_range эквивалентен index=date_range
# а первый аргумент np.random.rand(10) - случайные числа от 0 до 10
print(ser_3) # выведет наш дата фрейм
print()
print(ser_3>0.5) # выведет наш дата фрейм со значениями True False
print()
print(ser_3[ser_3>0.5]) # выведет только те строки, в которых выполняется это условие
print()
print(ser_3[(ser_3>0.6) | (ser_3<0.2)])
print()
print(ser_3[(ser_3>0.6) & (ser_3<0.2)])
print()

# Сортировки
print('Сортировка')
print(ser_3.sort_index()) # сортировка по индексу
print()
print(ser_3.sort_values()) # сортировка по значению
# эти объекты не изменяют исходный датафрейм

#       Операции с Series
# тип pd.Series можно модифицировать проще, чем стандартный list из Python
print(ser_3 + 100)
print(np.exp(ser_3)) # применили Экспоненту к нашему дата фрейму sеr_3
print()

term_1 = pd.Series(np.random.randint(0, 10, 5))
term_2 = pd.Series(np.random.randint(0, 10, 6))
print(term_1, '\n')
print(term_2)
print()
print(term_1 + term_2) # может складывать массивы разных размеров, но если один датафрейм больше другого.
# то на итоговый датафрейм получится со значениями Nan в тех ячейках, которых нет в одном из датафреймах и тип данных будет меняться на float64

print(term_1.shape) # выдает число строк датафрейма
print()



#           pd.DataFrame

# Создание и основные объекты

    #1) из словаря - ключ соответствует названию колонки

some_dict = {'one': pd.Series([1,2,3], index=['a','b','c']),
             'two': pd.Series([1,2,3,4], index=['a','b','c','d']),
             'three': pd.Series([5,6,7,8], index=['a','b','c','d'])}
df = pd.DataFrame(some_dict)
print(df)
print()

    #2) из списка списков с аргументом columns
some_array = [[1,1,4], [2,2,5], [3,3,6],[np.nan, 4,7]] # каждый вложенный списко это строка
df = pd.DataFrame(some_array, index=['a','b','c','d'], columns=['one', 'two', 'three'])
print(df)
print()

print(df.values) # извлекает все значения из дата фрейма в список списков
print(df.columns) # выведет название колонок - Index(['one', 'two', 'three'], dtype='object')
# и индексы и столбцы можно изменить задав новый список df.columns или df.index
print()


            # Индексирование Датафрейма
    #1) по колонкам
print('Индексирование Датафрейма')
print('По Колонкам')
first_column = df['one'] # на выходе Series
print(first_column, type(first_column))
subset_dataframe = df[['one','two']] # на выходе DataFrame
print(subset_dataframe)
print()

    #2) по строкам
# По номеру к строкам обращаться нельзя
print('По строкам')
print(df[:1]) # выведет первую строку
print(df[1:4]) # выведет 2,3,4 строки
print()

    #3) Уриверсальное индексирование: .loc и .iloc

print('iloc \n', df.iloc[1:3, :2]) # первый аргумент это строки, второй аргумент - это столбцы (строки - 3 не включительно)
print('loc \n', df.loc['a':'c', ['one', 'two']]) # первый аргумент это строки, второй аргумент - это столбцы (строки - 3 включительно)

    #4) Модификация Датафрейма
df['new_column'] = [5,3,6,3]
print(df)
print()


                # ТИТАНИК
print('Титаник')
titanik = pd.read_csv('https://www.dropbox.com/s/lyzcuxu1pdrw5qb/titanic_data.csv?dl=1', index_col='PassengerId') # столбец PassengerId использовали в качестве индекса
print(titanik.head(3))
print()
print('метод .shape',titanik.shape, '\n') #  выведет размер датафрейма
print('метод .info')
print( titanik.info()) # выведет название столбцов, сколько в каждом из них не пустых элементов и тип данных в каждом столбце
print(titanik.describe()) # выводит аналитические данные
print()

# Задание 1
# Опишите данный датасет: какое распределение женщин/мужчин в нем? Сколько пассажиров ехало в кaждом классе? какой средний/минимальный/максимальный возраст пассажиров?
print('Задание 1')
print('Считаем количество мужчин и женщин')
print(titanik.groupby('Sex').agg({'Sex': 'count'}), '\n')
print(titanik.Sex.value_counts())

print('Считаем распределение пассажиров по классам')
print(titanik.groupby('Pclass').agg({'Pclass': 'count'}), '\n')
print(titanik.Pclass.value_counts())

print('Считаем минимальное, среднее и максимальное значение возраста пассажиров')
print(titanik.Age.min())
print(titanik.Age.mean())
print(titanik.Age.max())


        # Задача 2
# Сгруппируйте записи по классам пассажиров, в каждой группе посчитайте средний возраст

print(titanik.groupby('Pclass').agg({'Age': 'mean'}))
# titanik_passengers.groupby(['Pclass'])['Age'].mean()

# Слияние таблиц

# 1) слияние таблиц по индексу метод называется pd.join.

df_2 = pd.read_csv('https://www.dropbox.com/s/v35x9i6a1tc7emm/titanic_surv.csv?dl=1')
print(df_2.head())

#        Задача 3
# Слейте два дата сета по колонке индекса

df_2.index = np.arange(1, 892) # присвоили индекс от 1 до 891

df_2 = df_2.sample(frac=1) # метод sample возвращает подвыборку из исходной нашей выборки, т.е вернет часть датасета,
# но если указать frac=1, то он вернет дата сет целиком, но в перемешанном сотоянии
print(df_2.head())

titanik = titanik.join(df_2) # слияние двух датафреймов - вызываем первый датафрейм а в методе join в аргументе указываем второй датафрейм
print(titanik.head())

#       Задача 4
# Сколько всего выживших паcажиров? Выживших пассажиров по каждому из полов? Постройте матрицу корреляий факта выживания, пола и возраста.

print('\nВыживших', titanik['Survived'].sum())
print(titanik['Survived'].value_counts())
print()
print(titanik.groupby('Sex').agg({'Survived': 'sum'}))
# print(titanik.groupby('Sex')['Survived'].sum())

# строим матрицу кореляции
corr_data = titanik[['Sex', 'Age', 'Survived']]
corr_data['Sex'] = (corr_data['Sex'] == 'female').astype(int) # заменили male female на 0 и 1
print(corr_data)

print(corr_data.corr()) # .corr() выводит матрицу кореляции

import seaborn as sns
from matplotlib import pyplot as plt

sns.heatmap(corr_data.corr(), annot=True, cmap='coolwarm', vmin=-1, vmax=1, annot_kws={"size": 16})
plt.show()