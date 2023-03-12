

burd = int(input("введите общее кол-во журавлей: "))

if burd % 2 != 0:
    print("введено не правильное число")
else:
    burdKate = burd // 3
    resultPS = burdKate // 2
    burdKate += burdKate


print(f"Катя сделала {burdKate} журавлей, Сергей {resultPS} и Петя {resultPS}")
