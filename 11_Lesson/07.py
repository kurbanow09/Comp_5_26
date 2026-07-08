txt = input("Enter string: ")
for x in txt:
    if txt.count(x) == 1:
        print(x + " - single letter")