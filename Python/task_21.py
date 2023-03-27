

list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {
    "VII": "S005"}, {" V ": " S009 "}, {" VIII": " S007 "}]

# вариант 1
set_1 = set()
for el in list_1:
    for i in el:
        set_1.add(el[i].strip())
print(set_1)

# вариант 2
set_1 = set()
for el in list_1:
    for value in el.values():
        set_1.add(value.strip())
print(set_1)
