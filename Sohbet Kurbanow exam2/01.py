print("""
- - - Kofe Menu - - -
1-Espresso (15 TMT)
2-Capuchina (25 TMT)
3-Latte (30 TMT)
""")

sayla = int(input("Kofe gornusu saylan (1-3): "))
if sayla == 1:
    gerek = int(input("Size nace sany Espresso aljak?: "))
    print(f"size {gerek} sany Espresso aldynyz")
    print(f"Jemi  toleginiz: {gerek * 15}")
elif sayla == 2:
    gerek = int(input("Size nace sany Capuchina aljak?: "))
    print(f"size {gerek} sany Capuchina aldynyz")
    print(f"Jemi  toleginiz: {gerek *25}")
elif sayla == 3:
    gerek = int(input("Size nace sany Latte aljak?: "))
    print(f"size {gerek} sany Latte aldynyz")
    print(f"Jemi  toleginiz: {gerek * 30}")
else:
    print("Yalnys saylaw! Dine 1, 2 ya-da 3 girizin.")