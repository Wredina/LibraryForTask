# а, у, о, ы, и, э, я, ю, ё, е
""" 
"""


def filter_word(word, letter):
    return len(list(filter(lambda x: x in letter, word)))


letters = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
text_list = list(input('введите текст: ').lower().split())
print(text_list)
if set(map(lambda x: filter_word(x, letters), text_list)) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')
# filter_text = set(map(lambda x: filter_word(x, letters), text_list))
# print(filter_text)
