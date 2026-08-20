
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

# with open("Book.txt", "r") as fayl:
#     a = fayl.read().split()
#     word = input("Enter a word")
#     if word in a:
#         print(f"Amount of the word:{a.count(word)}")
#     else:
        # print("The word is not in file")
# with open("Book.txt", "r") as fayl:
#     a = fayl.read().split()
#     letter = input("Enter a letter:")
#     for i in a:
#         if i.startswith(letter):
#             print(f"{i}")

# l = 0
# d = 0
# with open("Book.txt", "r") as fayl:
    # a = fayl.read().split()
#     for i in a:
#         if i.isalpha():
#             l += 1
#         elif i.isnumeric():
#             d += 1
# print(f"Amount of letters {l}")
# print(f"Amount of diggits {d}")

# with open("Book.txt", "r") as fayl:
#     a = fayl.read()
    
# with open("Book.txt", "w") as fayl:
#     fayl.write(a.upper())

# A = [55, 100, 65, 95, 80]
# in_uly = max(A)
# in_Kici = min(A)
# jemi = sum(A)
# ortaca = jemi / len(A)
# with open("Numbers.txt", "w") as fayl:
#     fayl.write(f"In uly san: {in_uly}\n")
#     fayl.write(f"In kici san: {in_Kici}\n")
#     fayl.write(f"Jemi: {jemi}\n")
#     fayl.write(f"Ortaca: {ortaca}\n")

A = [-69, 70, 92, -94, 94, 99, 10, -15, 17, -25]
