s, n = (int(x) for x in input().split())
if n <= s <= 9 * n:
    res = ""
    while s - 1 <= 9 * (n - 1):
        res += "1"
        s -= 1
        n -= 1
    if s != 9 * n and n > 0:
        x = s - 9 * (n - 1)
        res += str(x)
        s -= x
        n -= 1
    while n > 0:
        res += "9"
        n -= 1
    print(res)
else:
    print("impossible")

