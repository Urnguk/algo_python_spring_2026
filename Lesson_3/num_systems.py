# x = int(input())
# base = int(input())

# res = ""
# alphabet = "0123456789ABCDEF"
# while x > 0:
#     res = alphabet[x % base] + res
#     x //= base

# print(res)

# s = input()
# base = int(input())
# alphabet = "0123456789ABCDEF"

# res = 0
# for i in range(len(s)):
#     res *= base
#     res += alphabet.index(s[i])

# print(res)

# s = input()
# base = int(input())
# res = int(s, base)
# print(res)

s = "opej42noie0rv0"
for x in s:
    if x.isalpha():
        print(x)

