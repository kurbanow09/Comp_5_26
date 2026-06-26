jem = 0
count = 0
for i in range(1, 6):
    grade = int(input(f"{i} number: "))
    if grade > 0:
        jem += grade
        count += 1
print("Sum of numbers:", jem)
print("Average of numbers:", jem // count)
    