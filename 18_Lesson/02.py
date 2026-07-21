 import random
 A=["rock", "paper","scissors"]
 computer =0
 p =0

 while True:
     comp=random.choice(A)
     player=input("rock paper or scissors? ").lower()
     if player == "rock":
         if comp=="rock":
             print("Tie")
         elif comp=="paper":
             print("Computer Won, paper covers rock!")
             computer+=-0
         elif comp=="scissors":
             print("You won, rock smashes scissors!")
             p+=1
     elif player == "paper":
         if comp=="paper":
             print("Tie")
         elif comp=="scissors":
             print("Computer Won, scissors cut paper!")
             computer+=1
         elif comp=="rock":
             print("You won, paper covers rock!")
             p+=1
     elif player == "scissors":
         if comp=="scissors":
             print("Tie")
         elif comp=="rock":
             print("Computer Won, rock smashes scissors!")
             computer+=1
         elif comp=="paper":
             print("You won, scissors cut paper!")
             p+=1
     elif player=="quit":
         print(f"Computer:{computer}")
         print(f"Player:{p}")
         if computer>p:
             print("Sorry! Computer Won!")
         elif computer==p:
             print("Draw")
         else:
             print("Congratulations! You won")
         break