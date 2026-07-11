coffee_shop = {
    "espresso": 25,
    "latte": 25,
    "americano": 20,
    "macchiato": 30,
    "cappuccino": 30
}

order = input("Kofeniň adyny giriziň: ")
if order in coffee_shop:
    print(coffee_shop[order])
else:
    print("not found")