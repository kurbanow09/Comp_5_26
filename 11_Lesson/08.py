txt = input("Enter string: ")
for x in txt:
    print(x + " - " + str(txt.count(x)) + " time")