import sys


sys.setrecursionlimit(3000)
sys.set_int_max_str_digits(7000)


def f(n):
    if n == 1:
        return 1
    elif n > 1:
        return n * f(n - 1)


print(f(2020) - f(2022) // f(2020))
