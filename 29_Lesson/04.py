class shop:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description
    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Description: {self.description}")
        print(f"*" * 15)
    def cheap(self):
        self.price -= 1000
        print(f"Laptop New Price: {self.price}")
    def expansive(self):
        self.price += 500
        print(f"Laptop New Price: {self.price}")
shop = shop ("Laptop", 15000, "High-performance laptop")

shop.show_info()
shop.cheap()
shop.expansive()
