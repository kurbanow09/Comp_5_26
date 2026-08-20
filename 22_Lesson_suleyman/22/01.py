
# with open("python.txt", "r") as fayl:
#     print(fayl.read())

# with open("Book.txt", "r") as fayl:
#     print(fayl.read())


# with open("python.txt", "a") as file:
#     file.write("\nHow are you\n")
#     file.write("Welcome")

# nace = int(input("Nace sany okuwcyn bar: "))
# with open ("okuwcylar.txt", "w") as fayl:
#     for i in range(1, nace + 1):
#         name = input(f"{i} okuwcyn ady: ")
#         fayl.write(f"{name}\n")
# name = input("Enter name, surname, age: ")
# with open("names.txt", "w") as file:
#     # file.write(f"{name}")

# with open ("names.txt" , "r") as fayl:
#     print(fayl.read())


# nace = int(input("Nace sapak okayan: "))
# with open("Kurslar.txt" , "w") as fayl:
#     for i in range(1, nace + 1):
#         name = input("Sapaklar:")
#         fayl.write(f"{name}\n")
# import random
# with open("sanlar.txt", "w") as file:
#     for i in range(1, 6):
#         file.write(f"{random.randint(1000, 9999)}\n")
# with open("sanlar.txt", "r") as file:
#     print(file.read())


# with open("okuwcylar.txt", "w") as file:
#     for i in range(1, 6):
#         name = input(f"{i} - adyny yazyn: ")
#         file.write(f"{i}. {name}\n")
# print("Fayla yazyldy")

# with open ("Book.txt", "r") as fayl:
#     a = fayl.read().split()
#     word = input("Enter a word:")
#     if word in a:
#         print(f"Amount of the word {a.count(word)} ")
#     else:
#         print("The word is not in the file")

# letter = input("Enter a letter")
# print(letter.startswith())


# with open ("Book.txt", "r") as fayl:
#     a = fayl.read().split()
#     letter = input("Enter a letter:")
#     for i in a:
#         if i.startswith(letter):
#             print(i)

# with open ("Book.txt", "r") as fayl:
#     a = fayl.read().split()
#     print(f"Amount of all letters: {len(a)}")

with open("Book.txt", "r") as fayl:
    a = fayl.read().split()
    word = input("Enter a word")
    if word in a:
        print(f"Amount of the word:{a.count(word)}")