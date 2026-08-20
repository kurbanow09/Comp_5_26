jemi = 0
haryt = int(input("Nace sany haryt: "))

for i in range(1, haryt + 1):
    bahasy = int(input(f"{i}-nji haryt (TMT):"))
    jemi += bahasy
skitka = jemi * 0.2 
print("=" * 30)
print(f"Harydyn jemi: {jemi} TMT")
print(f"Dukanyn 20% skitka: -{skitka} TMT")
print(f"Tolemeli sonky jemi summa:{skitka - jemi}")
print("=" * 30)