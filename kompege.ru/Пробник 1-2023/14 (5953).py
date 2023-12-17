for x in "0123456789ABCDEFG":
    if not (int(f"10{x}0", 17) + int(f"F0{x}FF", 17)) % 13:
        print(x, (int(f"10{x}0", 17) + int(f"F0{x}FF", 17)) / 13)
