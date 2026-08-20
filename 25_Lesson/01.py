print("Welcome to SmartMarket!")

menu = {
        "milk": {"category": "drinks", "price": 4},
        "bread": {"category": "bakery", "price": 2},
        "apple": {"category": "fruits", "price": 3},
        "egg": {"category": "dairy", "price": 5},
        "cheese": {"category": "dairy", "price": 6},
        "meat": {"category": "meat", "price": 12}
    }
orders = []
while True:
    print("--- Available Products ---")
    for i, j in menu.items():
        print(f"- {i} ({j['category'].capitalize()}): ${j['price']}")
    product = input("Enter product name (done): ").lower()
    if product == 'done':
        break
    elif product in menu:
        quantity = input(f"How many '{product}' would you like to buy?: ")
        if not (quantity.isdigit()) or int(quantity) < 0:
            print("Invalid input❌")
    elif product not in menu:
        print("This product is not in menu❌")
        continue
    orders.append({
        'name' : product,
        'price' : menu[product]['price'],
        'quantity' : int(quantity)
    })
    print(f"✅Added {quantity} x {product} to yours cart.")

print("==========================")
print("\tRECEIPT🧾")
print("==========================")
summa = 0
total_summa = 0
for i in orders:
    summa += i['price'] * i['quantity']
    print(f"{i['name']} x{i['quantity']} = %{summa}")
    total_summa += summa
print("---------------------")
print(f"Total Amout Due: &{total_summa}")