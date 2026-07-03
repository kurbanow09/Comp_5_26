import random
name = input("Adyn name: ")
jem1 = 0
jem2 = 0

print('''
Jemi 4 sorag
''')

for i in range(1, 5):
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    print(f"{i} - nji sorag\n{a} + {b} =?")
    jogap = int(input("Your answer: "))
    if jogap == a + b:
        print("corect!")
        jem1 += 1

    elif jogap != a + b:
        print(f"Your answer is incorecct! Corecct answer is {a + b}")

print(f"***{name}! Your Result***")
print("Quastion: 10")
print(f"Corecct answer: {jem1}")
print(f"{jem1 * 256 / 10}%")