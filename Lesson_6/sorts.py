# def bubble_sort(arr):
#     for i in range(len(arr) - 1):
#         flag = True
#         for j in range(len(arr) - 1 - i):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 flag = False
#         if flag:
#             return
        

# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         j = i
#         while j > 0 and arr[j] < arr[j - 1]:
#             arr[j], arr[j - 1] = arr[j - 1], arr[j]
#             j -= 1






# data = [3, 8, 0, -4, 2, 3, 3, 7, 1]
# insertion_sort(data)
# print(data)


# def count_sort(arr):
#     cnts = [0 for i in range(10)]
#     for i in range(len(arr)):
#         cnts[arr[i]] += 1
#     res = []
#     for j in range(len(cnts)):
#         res += [j] * cnts[j]
#     return res


# data = [0, 1, 2, 1, 1, 5, 6, 9, 3, 0]
# data = count_sort(data)
# print(data)

# def f(x):
#     return x[0]

# f = lambda x: x[0]
# print(f("abiu"))
# print(f([3, 7, 9]))

# arr = ["32", "1", "154", "17", "11", "12", "21"]

# arr.sort(key= lambda x: x[0])
# print(arr)


def bin_count_sort(data):
    l = 0
    for element in data:
        if len(element) > l:
            l = len(element)
    
    for digit in range(l):
        zeros = []
        ones = []
        for element in data:
            if len(element) > digit and element[-1-digit] == "1":
                ones.append(element)
            else:
                zeros.append(element)
        data = zeros + ones
        print(*data)

arr = [str(t) for t in input().split()]
bin_count_sort(arr)