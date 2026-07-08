while True:
    number = input("+993 ")
    if number.isnumeric() and len(number) == 8 and number[:2] in ["61", "62", "63", "64", "65", "71"]:
        print("Correct, Next step!")
        break
    else:
        print("Phone number is Incorrect!")