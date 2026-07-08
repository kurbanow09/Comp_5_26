maglumat = input("Tekst giriziň: ")

print("Diňe uly harplar:")
for symbol in maglumat:
    if symbol.isupper():
        print(symbol, end=" ")
print()  