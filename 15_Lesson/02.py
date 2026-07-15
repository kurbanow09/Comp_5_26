inventory = [
    {'name': 'laptop', 'price': 1200.00, 'stock': 65},
    {'name': 'Mause', 'price': 25.00, 'stock': 12},
    {'name': 'Keyboard', 'price': 75.00, 'stock': 51},
    {'name': 'Monitor', 'price': 300.00, 'stock': 0},
    {'name': 'Webcam', 'price': 45.00, 'stock': 38},
    {'name': 'Headhones', 'price': 150.00, 'stock': 55},
    {'name': 'Mausepad', 'price': 10.00, 'stock': 5}
]

print("Dükana hoş geldiňiz! (Çykmak üçin 'exit' ýazyň)")

while True:
    item_name = input("\nAljak harydyňyzyň adyny ýazyň: ").strip()

    if item_name.lower() == "exit":
        print("Sowda tamamlandy. Sag boluň!")
        break
    found = False

    for item in inventory: 
        if item['name'].lower() == item_name.lower():
            found = True
            
            if item['stock'] == 0:
                print(f"Bagyşlaň, {item['name']} gutardy (Stokda ýok).")
                break
                
            try:
                quantity = int(input(f"{item['name']}-dan näçe sany almak isleýärsiňiz: "))
            except ValueError:
                print("Sany diňe san görnüşinde ýazmalydyr!")
                break

            if quantity <= item['stock']:
                total_price = quantity * item['price']
                item['stock'] = item['stock'] - quantity
                print(f"Töleg: {total_price} manat. Galan haryt sany: {item['stock']}")
            else:
                print(f"Ýeterlik haryt ýok. Bar bolan: {item['stock']}")
            
            break  

    if not found:
        print("Bagyşlaň, bu atly haryt ýok.")