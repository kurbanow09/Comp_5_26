inventory = [
    {'name': 'laptop', 'price': 1200.00, 'stock': 65},
    {'name': 'Mause', 'price': 25.00, 'stock': 12},
    {'name': 'Keyboard', 'price': 75.00, 'stock': 51},
    {'name': 'Monitor', 'price': 300.00, 'stock': 0},
    {'name': 'Webcam', 'price': 45.00, 'stock': 38},
    {'name': 'Headhones', 'price': 150.00, 'stock': 55},
    {'name': 'Mausepad', 'price': 10.00, 'stock': 5}
]

well_stocked = []
low_stock = []

for item in inventory:
    if item['stock'] > 50:
        well_stocked.append(item['name'])
    elif 0 <= item['stock'] < 50:
        low_stock.append(item['name'])
    elif item['stock'] == 0:
        print(f"{item['name']} atly onum hazir yok. ")

print(f"well stock: {well_stocked}")
print(f"Low stock: {low_stock}")