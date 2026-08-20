sanaw = []
def Okuwcy_gos(id_name, name, surname, age, Course):
    print("=" * 30)
    print("GIRIZILEN OKUWCYLARYN SANA")
    print("=" * 30)
    sanaw.append({"id_name" : id_name, "name" : name, "surname" : surname, "age" : age, "course" : course})
    print("---> Gosuldy")
def sanaw_gor():
    for i in sanaw:
        print(f"ID: {i['id_name']} | Ady: {i['name']} Surname: {i['surname']} | Yasy: {i['age']} | Course: {i['course']}")
print("=== Okuwcy Maglumat Ulgamy ===")
print("Taze okuwcy gosmak ucin ID ornuna 'stop' yazyn.")
while True:

    id_name = input("ID Girizin: ").capitalize()

    if id_name == "Stop":
        break
    name = input("Ady: ").capitalize()
    surname = input("Familiyasy: ").capitalize()
    age = input("Yasy: ").capitalize()
    course = input("Kursy: ").capitalize()

    Okuwcy_gos(id_name, name, surname, age, course)
    
sanaw_gor()