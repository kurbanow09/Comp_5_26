maglumat = input("Tekst giriziň: ")

harplar = 0
uly_harplar = 0
kici_harplar = 0
sifrler = 0
bosluklar = 0

for symbol in maglumat:
    if symbol.isalpha():
        harplar += 1
        if symbol.isupper():
            uly_harplar += 1
        elif symbol.islower():
            kici_harplar += 1
    elif symbol.isdigit():
        sifrler += 1
    elif symbol.isspace():
        bosluklar += 1

print(f"Ähli harplar: {harplar}")
print(f"Uly harplar: {uly_harplar}")
print(f"Kiçi harplar: {kici_harplar}")
print(f"Sifrler: {sifrler}")
print(f"Boşluklar: {bosluklar}")