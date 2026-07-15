iki = []
uc = []
A = [18, 42, 600, 214, 86,  320, 99, 52, 901]
for i in A:
    if 0 < i < 100:
        iki.append(i)
    elif 100 <= i < 1000:
        uc.append(i)
print(iki)
print(f"Mukdary: {len(iki)}")
print(uc)
print(f"Mukdary: {len(uc)}")