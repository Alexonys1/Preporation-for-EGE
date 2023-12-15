import sys, functools


sys.setrecursionlimit(10000)


@functools.cache
def f(n):
    print("Вызов с", n)
    if 10_000 <= n:
        return n
    elif n < 10_000 and not n % 2:
        return f(n + 2) - 3
    elif n < 10_000 and n % 2:
        return f(n + 2) + 1


print("Ответ:", f(94) - f(80))
