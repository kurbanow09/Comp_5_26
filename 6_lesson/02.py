username = input("Username: ")
if username == "sohbet" or "ayhan":
    print("Correct username")
    password = input("Password: ")
    if password == "0990" or "1234":
        print("Welcome to the program")
    else:
        print("Incorrect password")
else:
    print("Incorrect username")