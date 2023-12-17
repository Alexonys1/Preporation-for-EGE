# Прочту файл
with open("17.txt", 'r') as file:
    all_numbers = tuple(map(int, file.readlines()))
    arithmetic_mean = sum(all_numbers) / len(all_numbers)


# Найду все нужные тройки и их максимальную сумму
threes = []
max_sum = 0
am = arithmetic_mean
for i in range(3, len(all_numbers) - 1):
    a: int = all_numbers[i - 2]
    b: int = all_numbers[i - 1]
    c: int = all_numbers[i]

    if (a < am or b < am or c < am) and \
            str(a).count('9') and \
            str(b).count('9') and \
            str(c).count('9'):
        threes.append((a, b, c))
        max_sum = max(a + b + c, max_sum)

# Выведу ответ
print("Ответ:", len(threes), max_sum)
