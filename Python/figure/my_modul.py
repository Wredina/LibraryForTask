# import this - привет от разрабов
# найти площадь фигуры P*r^2

def circle(r):
    return 3.14 * r**2


def rect(n, m):
    return n * m


def tri(h, x):
    return 0.5 * h * x


def main():
    print("Начало работы  my_modul")
    print(circle(5))
    print(rect(5, 6))
    print(tri(5, 6))
    print("Конец работы  my_modul")


if __name__ == "__main__":
    main()
