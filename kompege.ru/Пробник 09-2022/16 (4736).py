import sys

sys.setrecursionlimit(1500)  # Это необходимость


def f(n: int) -> int:
    if n == 1:
        return 1
    else:
        return n * f(n - 1) - 1


print(f(1000) // f(997))
# Сказано, что нужна только ЦЕЛАЯ часть,
# поэтому делю две дроби нацело.
