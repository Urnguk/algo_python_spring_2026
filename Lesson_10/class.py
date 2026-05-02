# M = [[0] * 5] * 5
# M = [[0 for j in range(5)] for i in range(5)]

# M[1][4] = 7

# for line in M:
#     print(*line)


# N = int(input())
# M = int(input())
# A = [[1 for j in range(M)] for i in range(N)]

# for i in range(1, N):
#     for j in range(1, M):
#         A[i][j] = A[i - 1][j] + A[i][j - 1]

# print(A[-1][-1])


# def LCS(s, g):
#     matrix = [[0 for j in range(len(g) + 1)] 
#               for i in range(len(s) + 1)]
#     for i in range(len(s)):
#         for j in range(len(g)):
#             if s[i] == g[j]:
#                 matrix[i + 1][j + 1] = matrix[i][j] + 1
#             else:
#                 matrix[i + 1][j + 1] = max(matrix[i][j + 1], 
#                                            matrix[i + 1][j])
#     return matrix[-1][-1]


# print(LCS("123456", "722233785"))


# def z_basic(s):
#     res = [0 for i in range(len(s))]
#     for i in range(1, len(s)):
#         j = 0
#         while i + j < len(s):
#             if s[j] == s[i + j]:
#                 j += 1
#             else:
#                 break
#         res[i] = j
#     return res

# def z(s):
#     res = [0 for i in range(len(s))]
#     l = 0
#     r = 0
#     for i in range(1, len(s)):
#         if i <= r:
#             p = i - l
#             if res[p] + i - 1 <= r:
#                 res[i] = res[p]
#                 continue
#             res[i] = r - i + 1
#         j = res[i]
#         while i + j < len(s):
#             if s[j] == s[i + j]:
#                 j += 1
#             else:
#                 break
#         res[i] = j
#         l = i
#         r = i + j
#     return res

# print(z("abrakadabra"))


def pi(s):
    res = [0 for i in range(len(s))]
    for i in range(1, len(s)):
        j = i - 1
        while res[j] > 0:
            if s[i] == s[res[j]]:
                res[i] = res[j] + 1
                break
            j = res[j] - 1
        if res[i] == 0 and s[i] == s[0]:
            res[i] = 1
    return res


print(pi("abrakadabra"))
            

