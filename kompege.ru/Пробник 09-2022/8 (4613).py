from itertools import product


numbers = product("012345678", repeat=5)

count = 0
for number in numbers:
    if not int(number[0]) % 2 and \
            not (int(number[-1]) == 1 or int(number[-1]) == 8) and \
            number.count('3') <= 1:
        count += 1

print("Answer:", count)
