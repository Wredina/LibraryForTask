"""

"""


def same_by(characteristic, objects):
    # list_1 = list(filter(characteristic, objects))
    # print(list_1)
    # if list_1 == 0 or ['']:
    #     return True
    # return False
    return len(set(map(characteristic, objects))) == 1


values = [0, 2, 10, 6]

if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
