name = input("Adyn name: ")
print(f"{name} isgarlerin yasyny giriz")
print("Eger cykmak islesen 'cyk' diyip yazmaly")
i = 1
while True:
    age = input(f"{i}-nji isgarin yasy")
    if age > 35:
        print(print(f"Uly isgarler {age}"))
    elif age < 35:
        print(print(f"kici isgarler {age}"))
    else:  
        print(print(f"kic"))