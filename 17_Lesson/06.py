import random 
player_score = 0
computer = 0

while True: 
    choice = input("Do you roll a dise? (yes/no): ")
    if choice == "yes":
        player = random.randint(1, 6)
        play = random.randint(1, 6)
        computer+=player
        player_score+=play
        print(f"Computer {player}")
        print(f"Player {play}")
    else:
        print("* * * Final Score * * *")
        print(f"Computer score: {computer}")
        print(f"Player score: {player_score}")
        if player_score < computer:
            print("You Lose!")
        elif player_score == computer:
            print("You Draws")
        else:
            print("You Win!")
        break