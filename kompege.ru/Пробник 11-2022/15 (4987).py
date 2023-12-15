def f(number: int, base: int):
    alphabet = "0123456789abcdefghijklmnopqrstuvwxyz"
    result = ''
    if number < base:
        return alphabet[number]
    else:
        return f(number // base, base) + alphabet[number % base]


for base in range(2, 300):
    print(f(110, base))
