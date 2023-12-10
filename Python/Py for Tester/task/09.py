# def key_params(** kwargs):
#     spam = {}
#     for key, value in kwargs.items():
#         if not isinstance(value, list | set | dict):
#             spam[value] = key
#         else:
#             spam[str(value)] = key
#     return spam


# params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
# print(params)

x = 42
y = 'text'
z = 3.1415
print(hash(x), hash(y), hash(z))
