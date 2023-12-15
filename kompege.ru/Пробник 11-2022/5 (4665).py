max_r = 0
for n in range(1, 16):  # n = [1; 15]
    bin_n = bin(n)[2:]  # Отрезаю "0b".

    if bin_n.count('1') % 2 == 0:  # Если сумма чётная.
        new_bin_n = "10" + bin_n[2:] + '1'
    else:  # Если нечётная.
        new_bin_n = "11" + bin_n[2:] + '0'

    max_r = max(int(new_bin_n, 2), max_r)

print(max_r)
