jem = 0
sany = 0

while True:
    san = int(input("Enter a number: "))
    if san == -1:
        break
    jem += san
    sany += 1

if sany > 0:
    ortaça = jem // sany 
    print(f"Sum of Numbers: {jem}")
    print(f"Average of Numbers: {ortaça}")