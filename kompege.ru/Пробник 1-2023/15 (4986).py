def div(n, m):
    if not n % m:
        return True
    else:
        return False


b = [n for n in range(50, 71)]

for a in range(1, 100_000):
    flag = True
    for x in range(1, 100_000):
        if not (div(x, a) or (div(x, 23) <= (x not in b))):
            flag = False
            break
    if flag:
        print(a)
