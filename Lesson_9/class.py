# def hanoi(n, s, f):
#     if n == 0:
#         return
#     tmp = 6 - s - f
#     hanoi(n - 1, s, tmp)
#     print(f"{s} -> {f}")
#     hanoi(n - 1, tmp, f)


# hanoi(4, 1, 3)


# def grasshopper(coins):
#     stairs = [0 for i in range(len(coins))]
#     stairs[0] = coins[0]
#     stairs[1] = coins[0] + coins[1]

#     for i in range(2, len(stairs)):
#         stairs[i] = coins[i] + min(stairs[i - 1], 
#                                    stairs[i - 2])
#     return stairs[-1]


# def grasshopper(coins):
#     stairs = [float("inf") for i in range(len(coins))]
#     stairs[0] = coins[0]

#     for i in range(len(stairs) - 1):
#         stairs[i + 1] = min(stairs[i] + coins[i + 1], 
#                             stairs[i + 1])
#         if i + 2 < len(stairs):
#             stairs[i + 2] = min(stairs[i] + coins[i + 2], 
#                                 stairs[i + 2])
#     return stairs[-1]
    

# def fib(n):
#     a, b = 1, 1
#     for i in range(n - 2):
#         a, b = b, a + b
#     return b



    