txt = input("Enter string: ")
letters = 0
capitals = 0
smalls = 0
numbers = 0
spaces = 0

for x in txt:
    if x.isalpha():
        letters += 1
        if x.isupper():
            capitals += 1
        else:
            smalls += 1
    elif x.isnumeric():
        numbers += 1
    elif x.isspace():
        spaces += 1

print("Letters:", letters)
print("Capital letters:", capitals)
print("Small letters:", smalls)
print("Numbers:", numbers)
print("Spaces:", spaces)