import pandas as pd
import numpy as np

# %matplotlib inline - команда позволяющая получать графики прямо в программе (действует в jupiter notebook)
import matplotlib.pyplot as plt
import seaborn as sns

students_performance = pd.read_csv('https://stepik.org/media/attachments/course/4852/StudentsPerformance.csv')
students_performance.columns=students_performance.columns.str.replace(' ','_')
#
# pd.set_option('display.max_columns', None) # убирает ограничение вывода количества столбцов на экран
# # pd.set_option('display.max_rows', None)    # убирает ограничение вывода количества строк на экран
# pd.set_option('display.width', None)        # подгоняет ширину дисплея
#
print(students_performance.head())
#
students_performance.math_score.hist()
students_performance.plot.scatter(x='math_score', y='reading_score')
ax = sns.lmplot(x='math_score', y='reading_score', hue='gender', data=students_performance, fit_reg=False)
ax.set_xlabels('Math score') # переназвали ось х в 'Math score'
ax.set_ylabels('Reading score') # переназвали ось y в 'Reading score'
# # hue - группирующая переменная (разобьет наш график по уникальным значениям колонки 'gender', соответственно на male и female
# # fit_reg=False - убирает регрессионную прямую(по умолчанию True)
# plt.show()

            #SCILLBOX

df = pd.DataFrame([[1968, 'Alabama', 0.0],
                   [1968, 'California', 2.1],
                   [1969, 'California', 0.66],
                   [1970, 'California', 1.65]
                   ], columns= ['Year', 'State', 'Salary'])
print(df)
series1 = df[df['State'] == 'California']['Salary'] # в качестве оси Х использует индексы
plt.plot(series1)
plt.figure(figsize=(20, 10))# задали размер окна графика
plt.show()
series2 = df[df['State'] == 'California'].set_index('Year')['Salary']
# .set_index('Year') - меняем индексы на нужную колонку
plt.plot(series2) # построить график плот по серии
plt.title('Заголовок') # Задаём заголовок графику\
plt.xlabel('Год') # задаём название оси Х
plt.ylabel('Минмальная зарплата') # задаём название оси У
plt.xticks(range(10), rotation=45) # задаём метки оси Х, rotation=45 - поворачивает метки на 45 гр.
plt.show()


plt.plot() - ( * args , scalex = True , scaley = True , data = None , ** kwargs ) -
    # *args(x, y, fmt) - координаты по х и у, по умолчанию равны range(len(x), range(len(y))
    # scalex = True , scaley = True  - масштаб по о Х и по У
    # data = None - данные по которым строится график
plt.bar() # - сравнение либо нескольких категориальных признаков, либо несколько категорий одного признака
    # . Ось X всегда категориальный признак
plt.pie(series, labels=series.index, autopct='%1.0f%%') # - график пирог
    # autopct='%1.0f%%' - подписывает доли графиков процентами, %1.0f%% - определяет количество цифр после запятой
plt.hist(series, bins=10) # - строит гистаграмму по серии, bins=10 - задаёт количество интервалов графика(по умолчанию 10)
    # - показывают распределение данных одного численного признака. Ось X всегда численные данные
plt.scatter(df['Year'], df['Salary'], c=['IsCoastal']) # - строит точечный график(на вход принимает 2 серии состоящие из чисел)\
    # c=['IsCoastal'] - параметр с обозначает, что будут использоваться разные цвета в зависимости от столбика 'IsCoastal'
            #Пример добавление легенды на
# df0  = df[df['IsCoastal'] == 0] # датафрейм из строк штатов без порта
# plt.scatter(df0['Year'], df0['Salary'], label='Not Coastal') # строим точечный график штатов без порта
#
# df1  = df[df['IsCoastal'] == 1] # датафрейм из строк штатов с портом
# plt.scatter(df1['Year'], df1['Salary'], label='Coastal') # строим точечный график штатов с портом
#
# plt.title('Минимальная зарплата по годам') # Ставим название графика
# plt.xlabel('Год') # Ставим название оси Х
# plt.ylabel('$/час') # Ставим название оси У
#
# plt.legend() # собирает label  и добавляет легенду
#
df[df['Year'] == 2017].sort_values('Salary', ascending=False).head(2)
# Смотрим первые два штата в 2017 году с максимальной зарплатой

               # Нахождение 5%-ого перцентиля
df['значение'].value_counts()[df['значение'].value_counts(normalize=True)> 0.005] # - находим 5% перцентиль
# df['значение'].value_counts() - сортировка по наиболее часто встречающимся странам (страны и их количество)
# [df['значение'].value_counts(normalize=True)> 0.005] - условие фильтрации по 0.005


df_new = df_first.merge(df_second, how='left', on='название колонки') - соединяем один датафрейм с другим,
# по указанной колонки - on='название колонки'

            # Построение Графиков в Объектно-ориентированном стиле

    # figure - внешняя визуализация
    # axes - внутренности графика
plt.style.use('seaborn') # - полностью изменить стиль графика (!!!!ВЫЗЫВАЕТСЯ ДО ИНИЦИАЛИЗАЦИИ ГРАФИКА!!!!)
    plt.style.available # - посмотреть какие стили доступны для этой функции
fig, ax = plt.subplots(figsize=(12,8)) # получаем объекты figure и axes
    # figsize=(12,8) - определили размер окна графика
fig.suptitle('Название внешнего холста', y= 0.9) # -y=0.9 - изменяет расположение названия по вертикали
ax.plot(df['Seria_1'], df['Seria_2'], linewidth=1) # , linewidth=1 - задаём толщину линии
ax.axvline(x=1999, color='green', linewidth=1, linestyle='--') # axvline - рисуем вертикальную линию
    # x=1999 - вертикальная линия будет находится на отметке 1999 по оси Х
    # color='green' - цвет линии будет зеленый
    # linewidth=1  - толщина линии 1
    # linestyle='--' - тип линии - пунктирный
ax.axvspan(xmin=df['Series_1'].min(), xmax=df['Series_1'].max(), color='green', alpha=0.2)
    # xmin - минимальное значение прямоугольной зоны выделения
    # xmax - максимальное значение прямоугольной зоны выделенияF
    # color - цвет зоны выделения
    # alpha - прозрачность зоны выделения
ax.set_title('Вводим название графика', pad=16, color='navy')
    # - pad - определяет отступ от графика до заголовка, по умолчанию равен 6
    # color='navy' - меняет цвет текста
    # backgroundcolor='lightgray' - меняет цвет фона текста
ax.grid(color='gray', linestyle='--', linewidth=1) # рисуем сетку
    # color='gray' - цвет сетки
    # linestyle='--' - стиль линий сетки
    # linewidth=1 - толщина линий сетки
ax.set_xlabel('Вводим название оси Х')
ax.set_ylabel('Вводим название оси У')
ax.set_xticks(list(range(df['Seria_1'].min(), df['Seria_1'].max(), 10)) + [df['Seria_1'].max()]) # - Меняем отсечки на оси Х
ax.legend() # - отображает легенду
plt.show() # - выводит график на экран и не возвращает дополнительной информации

# 1) Можно построить несколько графиков на одной системе координат:
        df1 = ...
        df2 = ...
        fig, ax = plt.subplots(figsize=(12,8))
        ax.plot(df1['Seria_1'], df1['Seria_2'], label='Название 1')
        ax.plot(df2['Seria_1'], df2['Seria_2'], label='Название 2')\

     # Построение гистограммы в Объектно-ориентированном стиле и изменение цвето одного из столбцов
n, bins1, patches = ax.hist(df['series_1'], label='Название', alpha=0.5, bins=20 ) # - строит гистограмму
        # df['series_1'] - принимает аргументом Серию
        # label='Название' - устанавливаем название для каждой гистограммы, если их несколько (необходимо для легенды)
        # alpha=0.5  - выставляем прозрачность от 0 до 1, где 1 - полностью не прозрачная
        #
        # n - это массив высот каждого столбца
        # bins=20 - может принимать либо число - и тогда на гистолграмме будет это число столбцов
                    # либо список чисел - и эти числа будут границами столбцов
        # patches - массив объектов соответствующих столбцам, те. список прямоугольников для каждого столбца свой прямоугольник
max_index = np.argmax(n) # - нашли индекс максимальной высоты
patches.patches[max_index].set_color('green') # - в нашей переменной patches хранится список столбцов,
        # patches[max_index] - в этом списке мы находим нужный прямоугольник, по индексу
        # .set_color('green') - присваиваем указанному прямоугольнику нужный цвет - green
# 2) Складывание отсечек при построении двух гистограмм:
        df1 = ...
        df2 = ...
        fig, ax = plt.subplots(figsize=(12,8))
        _, bins1, _ = ax.hist(df1['series_1'], label='Название', alpha=0.5)
        _, bins2, _ = ax.hist(df2['series_1'], label='Название', alpha=0.5)
            # - метод hits() возвращает 3 объекта, нам нужен только второй объект bins
        ax.set_xticks(list(bins1) + list(bins2)) # - получаем отсечки из двух списков отсечек bins1 и bins2
        ax.tick_params(axis='x', rotation=45) # - настройки отсечек
            # axis='x'   - настройки отсечек по оси Х
            # rotation=45 - поворот текста отсечек
# 3) Перестраиваем гистограммы что бы ширина столбцов у двух гистограмм была одинаковой:
    df1 = ...
    df2 = ...
    fig, ax = plt.subplots(figsize=(12,8))
    _, bins1, _ = ax.hist(df1['series_1'], label='Название', alpha=0.5, bins=20)
    ax.hist(df2['series_1'], label='Название', alpha=0.5, bins=bins1)
    ax.set_xticks(list(bins1)) # - получаем отсечки из списка отсечек bins1
# 4) Построение графиков друг под другом:
    for year in [2000, 2010]:
        df = ...
        fig, ax = plt.subplots(figsize=(12,8))
        _, bins1, _ = ax.hist(df['series_1'], label=year, bins=20)
        ax.set_xticks(list(bins1)) # - получаем отсечки из списка отсечек bins1
# 5) Построение графиков на одном холсте:
    fig, axs = plt.subplots(nrows=2, ncols=1, sharex=True, figsize(12,6)) # в axs теперь хранится список графиков
        # nrows=2 - количество графиков в стобце
        # ncols=2 - количество графиков в строке
        # sharex=True - одни и те же отсечки по оси Х между всеми графиками
    df1 = ...
    df2 = ...
    _, bins1, _ = ax[0].hist(df1['series_1'])
    ax[1].hist(df2['series_1'], bins=bins1)
    ax[0].set_xticks(list(bins1)) # - получаем отсечки из списка отсечек bins1(теперь это нужно делать для каждого графика)
    ax[1].set_xticks(list(bins1)) # - получаем отсечки из списка отсечек bins1
# 6) Строим сетку по оси Х:
    for ax in axs:            # - перебираем графики
        ax.set_sticks(bins)   # - присваиваем список меток нашему текущему графику

        for bin in bins:      # - перебираем каждую метку в этом списке меток
            ax.axvline(x=bin) # - строим на этой метке вертикальную линию
# 7) Строим график  разным цветом по периодам
    # 7.1 Для построения линейного графика(plot) разными цветами нужно создавать под свой цвет отдельный график plot
    # 7.2 Для построения точечного графика(scatter) разными цветами необходимо:
        df = ...
        df['Color'] = 'green' # - создаём дополнительную колонку в датафрейме со значением green
        df.loc[df['Series_1'] < 4, 'Color'] = 'red'
        #         # - если в Series_1 значение меньше 4, то в столбце Color значение меняем на 'red'
        df.loc[(df['Color'] >= 4) & (df['Color'] < 7)] = 'yellow'
        #         # - если в Series_1 значение больше 4, но меньше 7, то в столбце Color значение меняем на 'yellow'
        fig, axs = plt.subplots(figsize(12,6))
        ax.scatter(df['Series_2', 'Series_1'], color=data['Color'])



                # SCILLBOX Seaborn
import seaborn as sns # - стандарт короткого названия sns
plt.style.use('seaborn') # - юпитер не всегда устанавливает стиль seaborn, поэтому установим его вручную
df[df['Year'].isin([2000, 2010])] # - фильтрует датафрейм по колонке 'Year' со значением 2000 и 2010
sns.histplot(data=df, x='Salary', hue='Year', alpha=0.3, multiple='dodge', size=5) # - data - выбирает датафрейм по которому будем строить,
# x - параметр Х для нашего графика,
# alpha - прозрачность
# hue - Признак по которому фильтровать данные для отдельных гистрограмм (различает по цветам)
# style -  Признак по которому фильтровать данные для отдельных гистрограмм (различает по типу линии)
# multiple='dodge' - расположение графиков на сетке координат. dodge - столбцы графика идут рядом друг с другом
# size - толщина линии на графике
# - сиборн автоматически привёл столбцы к одинаковой ширене, подобрал прозрачность, подписал обе оси, добавил легенду
ax = sns.histplot(data=df, x='Salary', hue='Year')  # можно присвоить к ax наш график histplot и затем работать с ним
# т.к sns.histpot возвращает объект класса axes
sns.scatterplot(data=df, x='Ось_Х', y='Ось_У', ax=ax) #- точечный график
sns.barplot(data=df, x='Ось_Х', y='Ось_У', ax=ax, ci=None) #- столбчатый график - барплот, ci - убираем доверительный интервал
sns.pairplot(df, corner=True, hue='От_чего_зависиит_оттенок') - # строит точечные графики зависимостей для всех пар численных признаков в датафрейме,
# corner - будет ли графики треугольником или квадратом(будет ли отражаться)
sns.distplot() # - устаревшая функция, за место неё есть histplot и displot

g = sns.FacetGrid(df, row='cut', col='color', hue='clarity') # построит сетку графиков(пустых)
g.map(sns.scatterplot, 'carat', 'price') # к каждому графику в сетке графиков "g",будет применяться sns.scatterplot,
g.add_legend() # - добавляем легенду
# row='cut' - количеству графиков по вертикали, будет соответствовать количество разных величин в колонке cut
# col='color' - количеству графиков по горизонтали, будет соответствовать колиичество разных величин в колонке color
# hue='clarity' - разбиваем все точки по цветам в соответствии со значениями в колонке clarity
# по оси Х  будут идти -'carat', а по оси У  будут идти 'price'

sns.load_dataset('diamonds') #  - загружаем встроенный датасет

sns.heatmap(df.isnull(), cbar=False, yticklabels=False, cmap='viridis') #- тепловая карта для оценки пропусков в датафрейме

        #Изменение стиля
sns.color_palette('husl', 7) # - смотрим цвета указанной палитры, в данном случае husl, и берем из нее 7 цветов
g = sns.FacetGrid(df, row='cut', col='color', hue='clarity', palette='rocket') # palette='rocket') - изменили палитру для hue
sns.barplot(data=df, x='color', y='price', ci=None, palette='dark', alpha=0.4, saturation=200, linewidth=5, edgecolor='black')
# ci=None, - убираем доверительный интервал
# palette='dark', - выбираем палитру dark
# alpha=0.4,  - делаем прозрачность 0.4
# saturation=200, - добавляем насыщенности
# linewidth=5, - добавляем обводку линиями
# edgecolor='black') - цвет линий вокруг столбцов black

.set # - тоже самое что и sns.set_theme
sns.set_theme(context='notebook', style='darkgrid', palette='deep', font='sans-serif', font_scale=1, color_codes=True, rc=None)