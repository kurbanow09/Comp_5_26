number = int(input("Enter a number: "))
if number % 2 == 0 and number < 10:
    print("1 digit even number")
elif number % 2 != 0 and number < 10:
    print("1 digit odd number")
elif number % 2 == 0 and number >= 10:
    print("2 digit even number")
elif number % 2 != 0 and number >= 10:
    print("2 digit odd number")
elif number > 1  or number >= 100:
    print("Invalid input")