import datetime
now = datetime.datetime.now()
name = input("Enter name: ").capitalize()

if 5 < int(now.strftime("%H")) < 12:
    print(f"Good Morning {name}")
elif 13 < int(now.strftime("%H")) < 18:
    print(f"Good Afternoon {name}")
elif 18 < int(now.strftime("%H")) < 20:
    print(f"Good Evening {name}")
else:
    20 < int(now.strftime("%H")) < 23 and 0 < 5
    print(f"Good Night {name}")