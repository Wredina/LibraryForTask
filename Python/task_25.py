

word = input("введите слово: ").split()
my_dict = dict()

for letter in word:
    print(letter, end="")
    if letter not in my_dict:
        my_dict[letter] = 0
    else:
        my_dict[letter] += 1
        print("_", my_dict[letter], sep="", end="")
    print(end=" ")
