sanaw = []
def Okuwcy_gos(name, age):
    sanaw.append({"name" : name, "age" : age})
    print("---> Gosuldy")
def sanaw_gor():
    for i in sanaw:
        print(f"Ady: {i['name']} | Yasy: {i['age']}")
print("=== Yonekey Okuwcy ulgamy ===")
print("Cykmak ucin 'stop' yazyn")
while True:
    name = input("Okuwcyn ady: ").capitalize()
    if name == "Stop":
        break
    age = input("Okuwcynyn Yasy: ")

    Okuwcy_gos(name, age)

sanaw_gor()