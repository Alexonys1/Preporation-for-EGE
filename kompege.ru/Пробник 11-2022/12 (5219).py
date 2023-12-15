def f(n, m):
    return True if not n % m else False


b = [n for n in range(160, 181)]
for a in range(1, 10000):
    flag = True
    for x in range(1, 10000):
        if not((x in b) <= (f(x, 35) <= f(x, a))):
            flag = False
            break
    if flag:
        print("A:", a)
