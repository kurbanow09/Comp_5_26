m = {
    "espresso" : {"price" : 25, "Quantity" : 50},
    "Latte" : {"price" : 25, "Quantity" : 50},
    "Americano" : {"price" : 20, "Quantity" : 50},
    "Macchiato" : {"price" : 30, "Quantity" : 50},
    "Cappuccino" : {"price" : 30, "Quantity" : 50}
}

for i, j in m.items():
    print(f"\n{i}")
    for n, m in j.items():
        print(f"{n} - {m}")