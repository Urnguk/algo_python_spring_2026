# def func(x, y):
#     return x + y


# a, b = 1, 2
# res = func(b, a)
# print(res)


# def prime(value):
#     if value < 2:
#         return False
#     div = 2
#     while div ** 2 <= value:
#         if value % div == 0:
#             return False
#         div += 1
#     return True


# for x in range(100):
#     if prime(x):
#         print(x)


# def func(value):
#     for a in range(1, int(value ** (1 / 3)) + 1):
#         for b in range(1, a):
#             if a ** 3 + b ** 3 == value:
#                 return a, b
#     return "Impossible"

# res = func(28)
# print(res)

# N = int(input())
# A = []
# for i in range(N):
#     A.append(int(input()))

# N = int(input())
# A = [int(input()) for i in range(N)]
# print(A)

# # for i in range(len(A)):
# #     A[i] *= 2
# #     A[i] += 1
# # print(A)

# A = [2 * A[i] + 1 for i in range(len(A))]


# A = [int(x) for x in input().split()]

# for x in A:
#     print(x)


# A = [i ** 2 for i in range(10)]
# # print(" ".join([str(x) for x in A]))
# print(*A)

# N = int(input())
# A = [int(input()) for i in range(N)]
# j = int(input())

# B = [A[i] for i in range(len(A)) if A[i] > A[j]]
# print(len(B))

N = int(input())
sieve = [True for i in range(N + 1)]
sieve[0], sieve[1] = False, False

for i in range(2, len(sieve)):
    if sieve[i]:
        for j in range(i + i, len(sieve), i):
            sieve[j] = False

prime = []
for i in range(2, len(sieve)):
    if sieve[i]:
        prime.append(i)

print(" ".join([str(x) for x in prime]))