jemi_musderi = 44  
icerdakiler = []  
MAKS = 10  

print("# 3-nji mysal. Bank we nobatcy robot")
print("Cykmak ucin 'Q' basyn.\n")

while True:
    if len(icerdakiler) >= MAKS:
        print("\nBank doly! Yer bosatmak ucin bir musderi cykmaly.")
        cykan = input("Isi bitip cykan musderi (ya-da 'status'): ")
        
        tapyldy = False
        for m in icerdakiler:
            if m.lower() == cykan.lower():
                icerdakiler.remove(m)
                print(f"{m} bankdan cykdy. Taze adam girip biler.")
                tapyldy = True
                break
        if not tapyldy:
            print("Seyle musderi icerde yok. Gaytadan synanysyn.")
        continue

    giris = input("Maglumat (Ady Familiyasy): ").strip()

    if giris.upper() == 'Q':
        print(f"\nJemlendi. Jemi hyzmat: {jemi_musderi}")
        break

    if not giris:
        print("Bos bolmaly dal!")
        continue

    jemi_musderi += 1
    icerdakiler.append(giris)

    print(f"Printer: {jemi_musderi}:{giris}")
    print(f"Icerde: {len(icerdakiler)}/{MAKS} adam bar\n")