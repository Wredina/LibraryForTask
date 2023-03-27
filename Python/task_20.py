

text = input("введите слово: ").upper()

eng = 'qwertyuiopasdfghjklzxcvbnm'.upper()
rus = 'йцукенгшщзхъфывапролджэячсмитьбюё'.upper()

dict_points_en = {1: 'AEIOULNSTR', 2: 'DG',
                  3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}

dict_points_rus = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ',
                   3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}

if text[0] in eng:
    sum = 0
    for letter in text:
        for key, value in dict_points_en.items():
            if letter in value:
                sum += int(key)
else:
    sum = 0
    for letter in text:
        for key, value in dict_points_rus.items():
            if letter in value:
                sum += int(key)
print(sum)
