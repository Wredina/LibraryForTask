

lenghtСhoco = int(input("введите длину шоколадки: "))
widthСhoco = int(input("введите ширину шоколадки: "))
delChoco = int(input("сколько долек хотите отломить? "))

sizeChoco = lenghtСhoco*widthСhoco
if sizeChoco % 2 == 0:
    print("можно произвести один разлом шоколатки")
else:
    print("нельзя произвести один разлом шоколадки")
