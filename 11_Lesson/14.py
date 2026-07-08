maglumat = input("Tekst giriziň: ")

print("Gaýtalanmaýan harplar:")
for symbol in maglumat:
    if maglumat.count(symbol) == 1:
        print(symbol, end=" ")
print()