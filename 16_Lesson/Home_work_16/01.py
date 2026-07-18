import string

alphabet = string.ascii_lowercase

while True:
    isleg = int(input("\n1.To Encrypt\n2.To Decrypt\n3.Exit\nYour Choice: "))

    if isleg == 3:
        print("Thanks for using the program!")
        break
        
    elif isleg == 1:
        message = input("Enter message: ").lower()
        key = int(input("Enter key: "))
        message2 = ""  
        
        for i in message:
            if i.isalpha():
                yeri = (alphabet.index(i) + key) % 26
                message2 += alphabet[yeri]
            else:
                message2 += i
        print("Encrypted text: ", message2) 

    elif isleg == 2:
        message = input("Enter message: ").lower()
        key = int(input("Enter key: "))
        message2 = ""
        
        for i in message:
            if i.isalpha():
                yeri = (alphabet.index(i) - key) % 26
                message2 += alphabet[yeri]
            else:
                message2 += i
        print("Decrypted text: ", message2)

    else:
        print("Wrong command. Please choose 1, 2, or 3.")