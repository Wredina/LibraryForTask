

klassA = int(input('Количество учащихся в классе А: '))
klassB = int(input('Количество учащихся в классе B: '))
klassC = int(input('Количество учащихся в классе C: '))
if klassA % 2 != 0:
    klassA += 1
if klassB % 2 != 0:
    klassB += 1
if klassC % 2 != 0:
    klassC += 1
total_students = klassA + klassB + klassC
total_desks = total_students // 2
print(f"{total_desks} - нужно парт")
