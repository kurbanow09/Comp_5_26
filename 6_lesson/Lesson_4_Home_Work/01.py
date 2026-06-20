print("1 – Kupe")
print("2 – Plaskart")
which = int(input("Which: "))

place = int(input("Place: "))

if which == 1:
    if place % 2 == 0:
        print("2 floor")
    else:
        print("1 floor")

elif which == 2:
    if place % 2 == 0:
        print("2 floor")
    else:
        print("1 floor")

else:
    print("Nädogry saylow!")