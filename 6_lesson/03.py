eat = input("Dou you want eat? ")
if eat == "yes":
    money = int(input("How much money do you have got? "))
    if money >= 50:
        print("You can eat :) ")
    elif money < 50:
        print("Sorry but your money is not enough :( ")    
elif eat == "no":
    print("Thank you: ")
else:
    print("I didn't understand: ")            
