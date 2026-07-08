maglumat = input("Tekst giriziň: ")

hasaplananlar = []
for symbol in maglumat:
    if symbol not in hasaplananlar:
        print(f"'{symbol}' simwoly: {maglumat.count(symbol)} gezek")
        hasaplananlar.append(symbol)