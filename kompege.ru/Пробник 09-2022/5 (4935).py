def calc(number: int) -> int:
    bin_number = bin(number)[2:]

    summ = 0
    for num in bin_number:
        summ += int(num)

    if summ % 2:
        bin_number = "11" + bin_number[:-2] + "11"
    else:
        bin_number = "10" + bin_number[:-2] + "00"

    return int(bin_number, 2)


max_number = 0
for num in range(30):
    max_number = max(calc(num), max_number)

print("Answer:", max_number)
