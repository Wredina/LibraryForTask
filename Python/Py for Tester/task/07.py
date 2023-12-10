import decimal

items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}

max_weight = 1.0

backpack = {}
sum_back = 0
for name, weight in items.items():
    sum_back += weight
    if sum_back <= max_weight:
        backpack.update(dict([(name, weight)]))
    else:
        sum_back -= weight

print(backpack)
