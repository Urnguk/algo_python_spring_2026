a = int(input())
b = int(input())

while b != 0:
    # k = a % b
    # a = b
    # b = k
    a, b = b, a % b

print(a)
