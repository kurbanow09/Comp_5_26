number = int(input("Enter a number: " ))
if number > 0 and number % 2 == 0:
    print("Posotive, even")
elif number > 0 and number % 2 != 0:
    print("Posotive, odd")
elif number < 0 and number % 2 == 0:
    print("Negative, even")
elif number < 0 and number % 2 != 0:
    print("Negative, odd")
elif number == 0:
    print("zero") 