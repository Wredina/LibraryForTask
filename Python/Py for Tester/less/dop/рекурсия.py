# на примере фибоначи
def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n-1) + fib(n-2)


list_1 = []
for i in range(1, 10):
    list_1.append(fib(i))
print(list_1)


# на примере быстрой сортировки
# 1. array=[10,5,2] \\ #2. array=[5,2] \\ #3. array = [2]
def qoick_sort(array):
    if len(array) <= 1:  # 3. return [2] final
        return array
    else:
        pivot = array[0]  # 1. pivot = 10 \\ #2. pivot = 5

    # 1. less=[5,2] \\ #2. less=[2]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]  # 1.[] \\ #2.[]
    # преобразовали число pivot в список, что бы списки с ним складывались
    return qoick_sort(less) + [pivot] + qoick_sort(greater)
# 1.qoick_sort([5,2]) + [10] + qoick_sort([])
# #2. qoick_sort([2]) + [5] + qoick_sort([])


print(qoick_sort([10, 5, 2]))


# Сортировка слиянием: список делится всё время на 2, после чего происходит слияние
#        5,4,3,2,1
#     5,4,3  --  2,1
#    5,4 -- 3 -- 2 -- 1
#  5 -- 4 -- 3 -- 2 -- 1
#  4,5 -- 3 -- 1,2
#     3,4,5 -- 1,2
#        1,2,3,4,5

def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1


list_2 = [1, 6, 8, 4, 2, 8, 9, 48, 54, 12, 7, 6, 3]
merge_sort(list_2)
print(list_2)
