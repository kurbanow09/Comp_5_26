while True:
    name = input("Enter name: ")
    if name.isalpha():
        print("Hello " + name)
        break
    else:
        print("Only letters!")