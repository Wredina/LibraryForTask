

n = int(input('введите число больше 1: '))
fib1 = 0
fib2 = 1
count = 2
while fib2 < n:
    # 0, 1 = 1, 1+0 // 1, 1 = 1, 1+1 // 1, 2 = 2 , 2+1// 2, 3 = 3, 3 + 2 // 3, 5 = 5, 3 + 5
    fib1, fib2 = fib2, fib1 + fib2
    count += 1

if n == fib2:
    print(count)
else:
    print(-1)

# a = int(input('введите число больше 1: '))
# if a < 1:
#     print(-1)
# else:
#     num2 = 0
#     num = 0
#     i = 1
#     res = 2
#     while num2 <= a or num <= a or i <= a:
#         num2 = num + i
#         if num2 != a:
#             res += 1  # 1 = 0 + 1 // 5 = 3 + 2
#         else:
#             res += 1
#             break

#         num = num2 + i
#         if num != a:
#             res += 1  # 2 = 1 + 1 // 8 = 5 + 2
#         else:
#             res += 1
#             break

#         i = num + num2
#         if i != a:
#             res += 1  # 3 = 2 + 1 // 13 = 8 + 5
#         else:
#             res += 1
#             break
#     print(res)
