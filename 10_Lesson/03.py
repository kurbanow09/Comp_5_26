print("Pepsi is 7 manats")
jem = 0
while True:
    pay = int(input("Please pay: "))
    jem += pay
    print(f"You paid {jem} manats")
    if jem >= 7:
        print("Take a pepsi")
        print(f"Refund {jem - 7} manats")
        break