from itertools import product


count = 0
for word in product("Р*СЛ*Н", repeat=5):
    if word.count('*') == 1:
        print(word)
        count += 1
print("Ответ:", count)
