machina = {
    "espresso" : {"price" : 25, "Quantity" : 50},
    "latte" : {"price" : 25, "Quantity" : 50},
    "americano" : {"price" : 20, "Quantity" : 50},
    "macchiato" : {"price" : 30, "Quantity" : 50},
    "cappuccino" : {"price" : 30, "Quantity" : 50}
}

summa = 0
while True:
    print(f"{3 * '*'} Coffe Machina {3 * '*'}")
    for i, j in machina.items():
        print(f"{i.capitalize()} - {j}") 
        
    drink = input("What drink: ").lower()
    
    if drink == "quit":
        print(f"Money due: {summa} manats")
        break
    elif drink in machina:
        Quantity = int(input("How many: "))
        if Quantity > machina[drink]["Quantity"]:
            print(f"{drink.capitalize()} is not enough")
        else:
            summa += Quantity * machina[drink]["price"]
            machina[drink]["Quantity"] -= Quantity
            print(f"Added {Quantity} {drink}. Current total: {summa} manats\n")
    else:
        print(f"{drink} not is machina\n")