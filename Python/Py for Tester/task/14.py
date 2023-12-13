'''Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int, премия str с указанием процентов вида 10.25%.
В результате result получаем словарь с именем в качестве ключа и суммой премии в качестве значения.

Сумма рассчитывается как ставка умноженная на процент премии'''
# names = ["Alice", "Bob", "Charlie"]
# salary = [5000, 6000, 7000]
# bonus = ["10%", "5%", "15%"]

names = ["Eva", "David", "Frank"]
salary = [7500, 8000, 9000]
bonus = ["8%", "12%", "7%"]

result = {names[i]: round(
    salary[i] * float(bonus[i].strip('%')) / 100, 2) for i in range(len(names))}
print(result)

res = {names: salary * float(bonus.strip('%')) / 100 for names,
       salary, bonus in zip(names, salary, bonus)}

print(res)
