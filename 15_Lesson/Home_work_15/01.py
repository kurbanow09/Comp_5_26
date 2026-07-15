Library = {  
    101 : {"name" : "Perman", "author" : "A.Govshudov", "quantity" : 8},                                
    102 : {"name" : "Saylanan eserler", "author" : "G.Ezizov", "quantity" : 12},                                
    103 : {"name" : "Ykbal", "author" : "H.Deryayev", "quantity" : 6},                                
    104 : {"name" : "Leyli Mejnun", "author" : "N.Andalyp", "quantity" : 4},                                
    105 : {"name" : "Oylanma bayry", "author" : "K.Gurbannepesov", "quantity" : 9} 
}

while True:
    print("* * * * * Library * * * * *")
    print("1.Show")
    print("2.Get")
    print("3.Submit")
    print("4.Exit")
    
    choice = input("Your choice: ")
    
    if choice == "1":
        for k, v in Library.items():
            print(f"{k} - {v}")
            
    elif choice == "2":
        book_id = int(input("Book id: "))
        quantity = int(input("Book quantity: "))
        if book_id in Library:
            if Library[book_id]["quantity"] >= quantity:
                Library[book_id]["quantity"] -= quantity
                print("You have received book")
            else:
                print("Book Not Enough")
                
    elif choice == "3":
        book_id = int(input("Book id: "))
        quantity = int(input("Book quantity: "))
        if book_id in Library:
            Library[book_id]["quantity"] += quantity
            print("You have submitted book")
            
    elif choice == "4":
        print("Thanks for using Program")
        break
        
    else:
        print("Wrong command...")