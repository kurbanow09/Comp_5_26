import random 

player_score = 0

while True: 
    choice = input("Do you roll a dise? (yes/no): ")
    if choice == "yes":
        player = random.randint(1, 6)
        print(f"Player {player}") #4
        player_score+=player
    else:
        print(f"Player score: {player_score}")
        print("Goodbye")
        break