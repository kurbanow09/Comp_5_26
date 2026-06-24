x = int(input("How many numbers: "))
y = 0
for i in range(1,x+1):
    z = int(input(f"{i} number: "))
    y+=z
print(f"The sum: {y}")