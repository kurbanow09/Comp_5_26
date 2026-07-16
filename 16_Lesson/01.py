import random

sowly = 0
sowsuz = 0
coin = ["san", "surat"]
for i in range(1, 4):
    birzat = random.choice(coin)
    sayla = input(f"Ulanyjy saylan? (san_surat): ")
    print(f"Kumpyuterin saylan tarapy: {birzat}")
    if sayla == birzat:
        sowly += 1
    else:
        sowsyz += 1
print(f"{sowly} gezek sowly boldy!")
print(f"{sowsyz} gezek sowly boldy!")