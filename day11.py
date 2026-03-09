h = int(input("H = "))
m = int(input("M = "))
s = int(input("S = "))

ms = 0

if 0 <= h <= 23:
    if 0 <= m <= 59:
        if 0 <= s <= 59:
            m += h * 60
            s += m * 60
            ms += s * 1000

            print(ms)
else:
    print("ERR")