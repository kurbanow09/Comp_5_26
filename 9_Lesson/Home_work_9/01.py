while True:
    san = int(input("Enter a number: "))
    if san == -1:
        print("Thanks for using Program!")
        break
    kwadrat = san ** 2
    print(f"{san} the square is {kwadrat}")