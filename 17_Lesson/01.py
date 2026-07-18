import random
# print(random.random())
# print(random.uniform(1, 10))
# print(random.randint(1, 10))

students = [
    "Akmuhammet",
    "Annanazar",
    "Aýhan",
    "Bakymuhammet",
    "Begenç",
    "Çerkez",
    "Eldar",
    "Isa",
    "Kerimmyrat",
    "Mylaýym",
    "Myrat",
    "Pena",
    "Sähra",
    # "Şatlyk",
    "Selimberdi",
    "Söhbet",
    "Süleýman",
    "Yhlas"
]

# print(random.choice(students))
# print(random.sample(students, 3))

random.shuffle(students)

print(students)