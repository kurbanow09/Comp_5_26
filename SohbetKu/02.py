hasap = 0

nace = int(input("Nace kofya aljak: "))
for i in range(1, nace + 1):
    bahasy = int(input(f"{i}-njin bahasy: "))
    hasap += bahasy
    a = hasap * 0.1
print(f"Tolemeli bahan {hasap} tmt")
print(f"Skitka 10% bahan {hasap * 0.1} tmt")
print(f"indi tolemeli bahan {hasap - a} tmt")