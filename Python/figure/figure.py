import my_modul


def all_square():
    n = int(input("Введите кол-во фигур: "))
    for i in range(n):
        sum_square = 0
        fig = input("Введите тип фигуры(т,п,к): ")
        plus_minus = input("Ведите необходимое действие(+ , -): ")
        symbol = 1
        if plus_minus == "-":
            symbol = -1
        if fig == "т":
            width = int(input("Ведите основание : "))
            higth = int(input("Ведите высоту : "))
            sum_square += my_modul.tri(width, higth) * symbol
        elif fig == "п":
            width = int(input("Ведите ширину : "))
            higth = int(input("Ведите длинну : "))
            sum_square += my_modul.rect(width, higth) * symbol
        elif fig == "к":
            rad = int(input("Ведите радиус : "))
            sum_square += my_modul.circle(rad) * symbol
    return sum_square


print("Общая площадь фигуры:", all_square())
