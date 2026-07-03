while True:
    birth_year = input("Enter birth year: ")
    
    if birth_year.isdigit() and len(birth_year) == 4:
        age = 2024 - int(birth_year)
        print(f"You are {age} years old!")
        break
    else:
        print("Only numbers and length 4")