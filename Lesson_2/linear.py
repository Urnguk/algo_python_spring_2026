# n = int(input())
# summ = 0

# for i in range(n):
#     x = int(input())
#     summ += x

# print(summ)

# n = int(input())
# mult = 1

# for i in range(n):
#     x = int(input())
#     mult *= x

# print(mult)


# n = int(input())

# max = -float("inf")

# for i in range(n):
#     x = int(input())
#     if x > max:
#         max = x

# print(max)


# n = int(input())

# min_x = float("inf")

# for i in range(n):
#     x = int(input())
#     min_x = min(x, min_x)

# print(min_x)


# n = int(input())

# max_2 = -float("inf")
# max_1 = -float("inf")

# for i in range(n):
#     x = int(input())

#     if x > max_1:
#         max_2 = max_1
#         max_1 = x
#     elif x > max_2:
#         max_2 = x

# print(max_1, max_2)


# x = int(input())
# summ = 0

# while x!= 0:
#     summ += x
#     x = int(input())

# print(summ)


# for x in (3, 7, 5):
#     print(x)

# s = "4578"
# summ = 0

# for element in s:
#     summ += int(element)

# print(summ)


# x = -3578
# x = abs(x)
# summ = 0
# while x != 0:
#     summ += x % 10
#     x //= 10


# x = int(input())

# if len(str(abs(x))) == 3:
#     print("YES")
# else:
#     print("NO")

x = int(input())

if (99 < abs(x) 
      and abs(x) < 1000):
    print("YES")
else:
    print("NO")
