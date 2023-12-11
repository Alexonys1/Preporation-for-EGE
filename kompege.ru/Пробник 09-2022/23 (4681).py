def f(x: int, y: int) -> int:
    if x > y:
        return 0  # Таких путей нет.
    elif x == y:
        return 1  # Мы на месте.
    else:
        return f(x + 3, y) + f(x * 2, y)


print("Answer:", f(3, 27) * f(27, 63))
