# # m = {
# #     "espresso" : {"price" : 25, "quantity" : 50},
# #     "latte" : {"price" : 25, "quantity" : 50},
# #     "americano" : {"price" : 20, "quantity" : 50},
# #     "macchiato" : {"price" : 30, "quantity" : 50},
# #     "cappuccino" : {"price" : 30, "quantity" : 50},
# # }
# # # # print(m)
# # # print(m["latte"]["price"])
# # # print(Employees["Meret"])
# # for i, j in m.items():
# #     print(f"\n{i}")
# #     for n, m in j.items():
# #         print(f"{n} - {m}")




# # Employees = {

# #     "Rejep": {"position": "programmer", "region": "Ashgabat", "age": 20},
# #     "Meret": {"position": "teacher", "region": "Ashgabat", "age": 31},
# #     "Oraz": {"position": "accauntant", "region": "Ashgabat", "age": 40}
# # }

# # name = input("Employee Name: ").title()

# # if name in Employees:
# #     choice = input("Full information (yes/no): ").lower()
# #     if choice == "yes":
# #         print(Employees[name])
# #     elif choice == "no":
# #         info = input("position/region/age: ").lower()
# #         print(Employees[name][info])
# #     else:
# #         print("Invalid input")
# # else:
# #     print(name, "is not in Employees")



# # machine = {
# #     "espresso": {"price": 25, "quantity": 50},
# #     "latte": {"price": 25, "quantity": 50},
# #     "americano": {"price": 20, "quantity": 50},
# #     "macchiato": {"price": 30, "quantity": 50},
# #     "cappuccino": {"price": 30, "quantity": 50}
# # }
# # s = 0
# # while True:
# #     print("* * * COFFEE MACHINE * * *")
# #     for i,j in machine.items():
# #         print(f"{i} - {j}")
# #     drink = input("What drink: ").lower()
# #     if drink in machine:
# #         m = int(input("How many: "))
# #         if m > machine[drink]["quantity"]:
# #             print(f"{drink} is not enough")
# #         else:
# #             s += machine[drink]["price"]*m
# #             machine[drink]["quantity"] -= m

# A = { "Turkmenistan": { "Capital": "Ashgabat",
#                                        "Currency": "Manat (TMT)",
#                                        "Language": "Turkmen",
#                                        "Population": "7 million" },
     
#          "Uzbekistan":     { "Capital": "Tashkent",
#                                        "Currency": "Som (UZS)",
#                                        "Language": "Uzbek",
#                                        "Population": "37 million" },

#          "Kazakhstan":     { "Capital": "Astana",
#                                        "Currency": "Tenge (KZT)",
#                                        "Language": "Kazakh",
#                                        "Population": "20 million" },

#          "Kyrgyzstan":     { "Capital": "Bishkek",
#                                        "Currency": "Som (KGS)",
#                                        "Language": "Kyrgyz",
#                                        "Population": "7 million" },

#           "Tajikistan":      { "Capital": "Dushanbe",
#                                        "Currency": "Somoni (TJS)",
#                                        "Language": "Tajik",
#                                        "Population": "10 million"  } }

# for i in A.keys():
#     print(F" - {i}")
# while True:
#     s = input("Select Country: ").title()
#     if s in A:
#         print(f"Country: {s}")
#         print(f"Capital: {}")

# a = []
# b = []
# while True:
#     word = input("Enter the word: ")
#     if word == "0": 
#         break
#     elif word[0] == word[-1]:
#         a.append(word)
#     b.append(word)
# print(f"Girizilen sozler: {', '.join(b)}")
# print(f"Netije: {a}")
sozluk = {
    "apple": "яблоко",
    "book": "книга",
    "computer": "компьютер",
    "teacher": "учитель",
    "student": "студент",
    "water": "вода",
    "friend": "друг",
    "school": "школа",
    "language": "язык",
    "game": "игра"
}