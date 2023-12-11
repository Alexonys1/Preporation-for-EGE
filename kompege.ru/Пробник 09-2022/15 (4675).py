def f(x: int, a: int) -> bool:
    return (x % 6 == 0) <= (x % 10) or ((x + a) > 121)


for a in range(1, 1000):
    a_is_correct = True
    for x in range(1, 1000):
        if not f(x, a):
            a_is_correct = False
            break
    if a_is_correct:
        print("Answer:", a)
        break

