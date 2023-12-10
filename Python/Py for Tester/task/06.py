from collections import Counter


"""
В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.

Слова разделяются пробелами. Такие слова как don t, it s, didn t итд (после того, как убрали знак препинания апостроф) считать двумя словами.
Цифры за слова не считаем.

Отсортируйте по убыванию значения количества повторяющихся слов.
"""
"""Ожидаемый ответ:

[('lazy', 3), ('the', 2), ('fox', 2), ('dog', 2), ('quick', 1), ('brown', 1), ('jumps', 1), ('over', 1)]"""


text = "The quick brown fox jumps over the lazy dog. Lazy dog, lazy fox!"
words = []
word = ""
for el in text.lower():
    if el.isalpha():
        word += el
    else:
        if word:
            words.append(word)
        word = ''

c_word = Counter(words)
n_word = c_word.most_common(10)

print(c_word)
print(n_word)
