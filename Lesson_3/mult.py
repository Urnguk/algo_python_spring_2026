# s = input()
# res = 1
# cur_mult = ""

# for i in range(len(s)):
#     if s[i].isdigit():
#         cur_mult += s[i]
#     elif cur_mult != "":
#         res *= int(cur_mult)
#         cur_mult = ""

# if cur_mult != "":
#     res *= int(cur_mult)
# print(res)

s = input()
for x in set(s):
    if not x.isdigit():
        s = s.replace(x, " ")
s = [int(x) for x in s.split()]
res = 1
for x in s:
    res *= x
print(res)
