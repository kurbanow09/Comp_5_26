import os

while True:
    print("***** Students Information *****")
    print("1. View")
    print("2. Add")
    print("3. Remove")
    print("4. Exit")

    choice = input("Your choice: ")

    if choice == "1":
        print("--- Talyplaryn Sanawy ---")
        try:
            with open("Students.txt", "r") as fayl:
                content = fayl.read()
                if content:
                    print(content, end="")
                else:
                    print("Sanaw bos.")
        except FileNotFoundError:
            print("Fayl entak doredilmandir. Ilki taze talyp goshun.")

    elif choice == "2":
        id_number = input("Id Number: ")
        name = input("Name: ")
        surname = input("Surname: ")
        phone = input("Phone: ")
        address = input("Address: ")

        with open("Students.txt", "a") as fayl:
            fayl.write(id_number + " " + name + " " + surname + " " + phone + " " + address + "\n")

        print("Added successfully")

    elif choice == "3":
        id_number = input("Id Number: ")

        try:
            with open("Students.txt", "r") as fayl:
                lines = fayl.readlines()

            taze_sanaw = []
            tapyldy = False

            for line in lines:
                if not line.startswith(id_number):
                    taze_sanaw.append(line)
                else:
                    tapyldy = True

            if tapyldy:
                with open("Students.txt", "w") as fayl:
                    fayl.writelines(taze_sanaw)
                print("Removed successfully")
            else:
                print("Talyp tapylmady.")

        except FileNotFoundError:
            print("Fayl entak doredilmandir.")

    elif choice == "4":
        break

    print()