import random
ch = 3
comp = random.randint(1,10)
while True:
    print(comp)
    print(f" senin sansyn {ch}")
    guess = int(input("bir san yaz (1-10): "))

    if comp > guess:
        print("san uly")
    elif comp < guess:
        print("san kici")
    elif comp == guess:
        print("Dogry")
    


    ch -= 1
    if ch == 0:
        print(f"Utuldyn {comp}")
    break