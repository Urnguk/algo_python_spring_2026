# def factorial(n):
#     if n == 0:
#         return 1
#     return factorial(n - 1) * n


# print(factorial(5))


# def f(x):
#     if x == 0:
#         return
#     print(x)
#     f(x - 1)
#     print(x)


# f(5)


# def f(x):
#     if x == 0:
#         return 1
#     return g(x)


# def g(x):
#     return f(x - 1) * x



# print(f(5))


# 1, 1, 2, 3, 5, 8, 13, 21, ...


# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     return fib(n - 1) + fib(n - 2)


# print(fib(7))


# def fib(n):
#     a, b = 1, 1
#     for i in range(n - 1):
#         a, b = b, a + b
#     return a

# print(fib(50))


def make_exchange(money, coins):
    if money == 0:
        return 1
    if money < 0 or len(coins) == 0:
        return 0
    return make_exchange(money - coins[0], coins) + make_exchange(money, coins[1:])


print(make_exchange(4, [1, 2]))




