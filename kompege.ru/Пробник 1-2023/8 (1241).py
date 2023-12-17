from itertools import product


count = 0
for word in product("РУСЛАН", repeat=5):
    if word.count('У') <= 1 and word.count('А') <= 1:
        print(word)
        count += 1
print("Ответ:", count)
