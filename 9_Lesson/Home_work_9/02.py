jem = 0
while True:
    san = int(input("Enter a number: "))
    if san == -1:
        break
    jem += san

print(f"Sum of Numbers: {jem}")