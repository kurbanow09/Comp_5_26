while True:
    year = input("Enter birth year: ")
    if year.isnumeric() and len(year) == 4:
        age = 2024 - int(year)
        print("You are " + str(age) + " years old!")
        break
    else:
        print("Only numbers and length 4")