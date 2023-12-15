print("X Y W Z")

for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if (w <= ((x <= z) <= y)) == 0:
                    print(x, y, w, z)
