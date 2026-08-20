import datetime
now = datetime.datetime.now()
m = int(input("How many days: "))
for i in range(1, m + 1):
    print(f"{i} - {now.strftime('%d.%m.%Y %A')}")
    now += datetime.timedelta(days=1)