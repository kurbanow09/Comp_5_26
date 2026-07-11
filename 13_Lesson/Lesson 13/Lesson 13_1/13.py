# contact={
#     "Rejep":66112233,
#     "Meret":66445566,
#     "Oraz":66778899,

# }
# print(contact)

# print(contact["Rejep"])


# contact["Meret"]=66111222
# print(contact)


# contact.setdefault("Gurban",663343444)

# print(contact)

# contact.pop("Oraz")
# print(contact)

# for i in contact.keys():
#     print(i)

# for i in contact.values():
#     print(i)

# for i,j in contact.items():
#     print(f"{i}-{j}")

# number=input("Whose phone number").capitalize()
# if number in contact:
#     print(f"{number}-{contact.get(number)}")
# else:
#     print("Phone number not found")

# choice={
#     'espresso': 25,
#     'latte': 25,
#     'americano': 20,
#     'macchiato': 30,
#     'cappuchino': 30,
# }
# kassa=0
# print("Coffee Machine")
# for i,j in choice.items():
#     print(f"{i}-{j}")
# while True:
#     drink=input("What drink").lower()
#     if drink in choice:
#         how_many=int(input("How many"))
#         kassa+= how_many*choice[drink]
#     elif drink=="quit":
#         break
#     elif drink not in choice:
#         print(f"{drink} is not in coffee machine!")
# print(f"Money due:{kassa}-manats" )


# a={
#     "hello":"salam",
#     "apple":"alma",
#     "lemon":"limon",
#     "cat":"pisik",
#     "dog":"it",
#     "flag":"baydak",
#     "student":"okuwcy",
#     "family":"masgala",
#     "pen":"rucka",
#     "water":"suw",
#     "bread":"corek",
# }
# print("""
# 1. Show
# 2.Add
# 3.Edit
# 4. Delete
# 5.Exit
# """)
# while True:
#     choice=int(input("Your choice?"))
#     if choice==1:
#         for i,j in a.items():
#             print(f'{i}-{j}')
#     elif choice==2 :
#         eng=input("Enter the word in english:").lower()
#         tkm=input("Enter the word in Turkmen:").lower()
#         a.setdefault(eng,tkm)
#         print("Added succesfully")
#     elif choice==3:
#         eng=input("Enter the word in english:").lower()
#         tkm=input("Enter the word in Turkmen:").lower()
#         a[eng]=tkm
#         print("Edited successfully")
#     elif choice==4:
#         eng=input("Enter the word in english:").lower()
#         a.pop(eng)
#         print("Deleted succesfuly")
#     elif choice==5:
#         print("Thanks for using😁 ")
#         break
#     else:
#         print("Wrong commanad")
#         break
# a={
#     "alma":8,
#     "uzum":12,
#     "hurma":18,
#     "banan":25,
#     "nar":15,

# }
# for i,j in a.items():
#     print(f"{i}-{j}")
# kassa=0
# while True:
#     almak=input("Name almak isleyarsiniz?").lower()
#     if almak in a:
#         nace=float(input("Nace kg almak isleyarsiniz"))
#         kassa+=nace*a[almak]
#     elif almak=="quit":
#         break
# print(f"Siz {kassa} manat tolemeli")

# a={
#     "Meret": 67625495,
#     "Oraz": 67115599,
#     "Ashyr": 67625495,
# }
# print(a)

# a["Oraz"]=67384289
# print(a)

# for i,j in a.items():
#     print(f"{i}-{j}")

# a.pop("Ashyr")
# print(a)


# a=["Rejepov", "Meredowa","Orazova", "Gurbanov", "Ashyrov", "Saparova"]
# oglan=[]
# gyz=[]
# for i in a:
#     if i.endswith("a"):
#         gyz.append(i)
#     elif i.endswith("v"):
#         oglan.append(i) 
# print(oglan)
# print(gyz)


isgarler={"Mekan":{ "hunari": "programist",
                    "bilimi": "orta",
                    "yashy": 22},}
        "Oraz:" {"hunari":"hasaphy",
                "bilimi": "yokary",
                "yashy":30},

}

print(isgarler)
        