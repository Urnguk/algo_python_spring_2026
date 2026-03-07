n = int(input())
x = 2
while n > 0:
    div = 2
    prime = True
    while div ** 2 <= x:
        if x % div == 0:
            prime = False
            break
        div += 1
    if prime:
        n -= 1
    x += 1
print(x - 1)