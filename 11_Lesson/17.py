maglumat = input("Tekst giriziň: ")

jemi_sany = len(maglumat)
uly_harplar = 0
kici_harplar = 0

if jemi_sany > 0:
    for symbol in maglumat:
        if symbol.isupper():
            uly_harplar += 1
        elif symbol.islower():
            kici_harplar += 1

    uly_goterim = (uly_harplar / jemi_sany) * 100
    kici_goterim = (kici_harplar / jemi_sany) * 100

    print(f"Uly harplaryň göterimi: {uly_goterim:.2f}%")
    print(f"Kiçi harplaryň göterimi: {kici_goterim:.2f}%")
else:
    print("Gidilen tekst boş.")