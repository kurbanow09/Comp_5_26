import random

player = input("Player (number/picture) ").strip().lower()

if player in ["number", "picture"]:
    if player == "number":
        Comp = "picture"
    else:
        Comp = "number"
        
    print(f"Computer chose {Comp}")

    print("- " * 10)
    
    coin = random.choice(["number", "picture"])
    print(f"Tossed coin: {coin}")
    
    if player == coin:
        print("Congratulation! You Won!")
    else:
        print("Sorry! Computer Won!")
else:
    print("Invalid choice! Please type 'number' or 'picture'.")