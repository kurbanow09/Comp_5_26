san = int(input("How many: "))

print(f"How many: {san}")

i = 1
while True:
    
    belgi = "&" if i % 2 != 0 else "@"
    
    print(f"{i} " + f"{belgi} " * i)
    
    i += 1
    if i > san:  
        break