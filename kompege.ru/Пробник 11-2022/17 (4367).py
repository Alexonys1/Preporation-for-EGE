with open("17.txt", 'r') as file:
    all_numbers = list(map(int, file.readlines()))


# Нахожу минимальное число с особым условием
min_num = 100_000
for num in all_numbers:
    if not num % 8 and num != 8:
        min_num = min(num, min_num)


# Нахожу все пары
pairs = []
for i in range(1, len(all_numbers)):
    a = all_numbers[i-1]
    b = all_numbers[i]
    if not a % min_num and not b % min_num:
        pairs.append((a, b))  # В виде кортежа


# Нахожу пару из найденных пар с минимальной суммой элементов
min_sum = 100_000_000
for a, b in pairs:
    min_sum = min(a + b, min_sum)


# Нахожу, есть ли несколько пар с одинаковй минимальной суммой
founded_i = []
i = 0
for a, b in pairs:
    if (a + b) == min_sum:
        founded_i.append(i)
    i += 1


# Показываю ответ
min_i = min(founded_i)
print("Кол-во пар:", len(pairs))
print("Второй ответ:", max(pairs[founded_i[0]]))
