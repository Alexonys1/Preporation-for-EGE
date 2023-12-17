min_n = 100_000_000
for n in range(1, 100):
    bin_n = bin(2*n)[2:]
    bin_n += str(bin_n.count('1') % 2)
    bin_n += str(bin_n.count('1') % 2)
    bin_n = str(bin_n.count('1') % 2) + bin_n
    r = int(bin_n, 2)
    if r > 249:
        print(n, '-', r)
        min_n = min(n, min_n)

print("Ответ:", min_n)
