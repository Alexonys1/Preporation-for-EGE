print("X Y Z W")

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (((x <= z) <= y) or (not w)) == 0:
                    print(x, y, z, w)
