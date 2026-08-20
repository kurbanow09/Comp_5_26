try:
    with open("Students.txt", "r") as fayl:
        print((fayl.read()))
except FileNotFoundError:
    print("bolanok")