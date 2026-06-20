music = input("Listen to music? ")
if music == "yes":
    print("""
    < < < Music Player > > >
        1 - Country    
        2 -Clasical    
        3 - Rap   
    """)
    
    choise = int(input("Your choise: "))
    if choise == 1:
        print("You can listen to Country music")
    elif choise == 2:
        print("You can listen to Clasical music")
    elif choise == 3:
        print("You can listen to Rap music")
        
else:
    print("I didn't understand")

