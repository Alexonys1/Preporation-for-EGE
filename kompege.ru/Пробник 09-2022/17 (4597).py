# Читаю файл
with open("17.txt", 'r') as file:
    all_numbers = tuple(map(int, file.readlines()))
    min_number = min(all_numbers)


# Нахожу все нужные пары
correct_pairs = []
for i in range(len(all_numbers) - 1):  # Чтобы не выйти за границы.
    first_number = all_numbers[i]
    second_number = all_numbers[i+1]

    if first_number % 117 == min_number or \
            second_number % 117 == min_number:
        correct_pairs.append((first_number, second_number))


# Нахожу максимальную сумму элементов найденных пар
max_sum = 0
for first_number, second_number in correct_pairs:
    max_sum = max(max_sum, first_number + second_number)


# Вывожу ответ
print("Кол-во подходящих пар:", len(correct_pairs))
print("Максимальная сумма элементов пар:", max_sum)
