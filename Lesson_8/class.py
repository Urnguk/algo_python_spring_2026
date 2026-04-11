# def bin_search(arr, value):
#     left = 0
#     right = len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == value:
#             return True
#         if arr[mid] < value:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return False


# def bin_search(arr, value, left=0, right=None):
#     if right == None:
#         right = len(arr) - 1
#     if right < left:
#         return False
#     mid = (left + right) // 2
#     if arr[mid] == value:
#         return True
#     if arr[mid] < value:
#         return bin_search(arr, value, mid + 1, right)
#     return bin_search(arr, value, left, mid - 1)


# A = [1, 3, 0]
# print(bin_search(A, 2))


# def MergeSort(arr):
#     if len(arr) <= 1:
#         return arr
#     return Merge(MergeSort(arr[:len(arr) // 2]), 
#                  MergeSort(arr[len(arr) // 2:]))


# def MergeSort(arr): return arr if len(arr) <= 1 else Merge(MergeSort(arr[:len(arr) // 2]), MergeSort(arr[len(arr) // 2:]))


# def Merge(A, B):
#     i = 0
#     j = 0
#     res = []
#     while i < len(A) and j < len(B):
#         if A[i] <= B[j]:
#             res.append(A[i])
#             i += 1
#         else:
#             res.append(B[j])
#             j += 1
#     # while i < len(A):
#     #     res.append(A[i])
#     #     i += 1
#     # while j < len(B):
#     #     res.append(B[j])
#     #     j += 1
#     res += A[i:] + B[j:]
#     return res
        

# def Merge(A, B):
#     i = 0
#     j = 0
#     res = []
#     A.append(float("inf"))
#     B.append(float("inf"))
#     for k in range(len(A) + len(B) - 2):
#         if A[i] <= B[j]:
#             res.append(A[i])
#             i += 1
#         else:
#             res.append(B[j])
#             j += 1
#     return res


# A = [3, 8, 9, 12, 3, 0, -5, 7, 7, 7, 7, 7]

# print(MergeSort(A))


# def qsort(A): return A if len(A) <= 1 else (qsort([x for x in A if x < A[0]]) + [x for x in A if x == A[0]] + qsort([x for x in A if x > A[0]]))

import random
import time

def qsort(A, l=0, r=None):
    if r is None:
        r = len(A) - 1
    if r <= l:
        return
    p = A[random.randint(l, r)]

    i = l
    j = r

    while i <= j:
        while A[i] < p:
            i += 1
        while A[j] > p:
            j -= 1
        if i <= j:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
    qsort(A, l, j)
    qsort(A, i, r)


A = [random.randint(0, 10 ** 6) for i in range(10 ** 6)]
t1 = time.time()
qsort(A)
t2 = time.time()
print(t2 - t1)
