from itertools import product


count = 0
for word in product("АРБУЗ", repeat=6):
    word = "".join(word)
    if word.count("АА") == 1 and \
            word.count("А") == 3 and \
            not word.count("ААА"):
        count += 1
        print(word)

print("Ответ:", count)
