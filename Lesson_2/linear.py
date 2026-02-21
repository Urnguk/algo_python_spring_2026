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

# x = int(input())

# if (99 < abs(x) < 1000):
#     print("YES")
# else:
#     print("NO")

# x = int(input())
# y = int(input())
# z = int(input())

# a = min(x, y, z)
# c = max(x, y, z)
# b = x + y + z - a - c

# if c >= a + b:
#     print("impossible")
# elif c ** 2 > a ** 2 + b ** 2:
#     print("obtuse")
# elif c ** 2 == a ** 2 + b ** 2:
#     print("right")
# else:
#     print("acute")

# x = int(input())
# while x % 2 == 0:
#     x //= 2
# if x == 1:
#     print("YES")
# else:
#     print("NO")


summ = 0
x = int(input())
last_odd = False
while x != 0:
    if last_odd:
        summ += x
    last_odd = x % 2 != 0
    x = int(input())

if summ == 0:
    print(-1)
else:
    print(summ)
