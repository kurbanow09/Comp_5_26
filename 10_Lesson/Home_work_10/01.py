cups = 50
price_per_cup = 6

while True:
    if cups <= 0:
        print("Sorry, out of coffee! The machine is now stopping.")
        break

    print(f"Coffee machine has {cups} cups of coffee")
    print(f"A cup of coffee is {price_per_cup} manats")
    
    requested_cups = int(input("How many cups of coffee? "))
    
    if requested_cups <= 0 or requested_cups > cups:
        print(f"Invalid number! We only have {cups} cups left. Try again.\n")
        continue
        
    total_cost = requested_cups * price_per_cup
    
    inserted_money = int(input(f"Please, pay {total_cost} manats: "))
    
    while inserted_money < total_cost:
        missing_amount = total_cost - inserted_money
        print(f"Not enough money! {missing_amount} manats missing. You need to pay {missing_amount} manats more.")
        additional_money = int(input(f"Please add more money: "))
        inserted_money += additional_money

    print("Please, take your coffee!")
    
    refund = inserted_money - total_cost
    if refund > 0:
        print(f"Refund: {refund} manats!")
        
    cups -= requested_cups
    print("-" * 30)