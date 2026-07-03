while True:
    name = input("Enter name: ")
    
    if name.isalpha():
        print(f"Hello {name}")
        break
    else:
        print("Only letters!")