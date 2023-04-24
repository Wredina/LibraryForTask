"""

"""


def find_farthest_orbit(list_of_orbits):
    arr = list(filter(lambda x: x[0] != x[1], list_of_orbits))
    arr_2 = list(map(lambda x: x[0]*x[1], arr))
    max_s = max(arr_2)
    i_max = arr_2.index(max_s)
    return (arr[i_max])


# def find_farthest_orbit(list_of_orbits):
#   i_max = 0
#   s_max = 0
#   for i, el_tuple in enumerate(list_of_orbits):
#     s_cur = el_tuple[0] * el_tuple[1]
#     if el_tuple[0] != el_tuple[1] and s_max < s_cur:
#       i_max = i
#       s_max = s_cur
#     return list_of_orbits[i_max]


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
