while True:
    pas = input("Enter Password: ")
    letters = 0
    numbers = 0
    for x in pas:
        if x.isalpha():
            letters += 1
        elif x.isnumeric():
            numbers += 1
            
    if len(pas) < 6:
        print("At least length 6")
    elif numbers < 2:
        print("At least numbers 2")
    elif letters < 4:
        print("At least letters 4")
    else:
        print("Accepted Password")
        break