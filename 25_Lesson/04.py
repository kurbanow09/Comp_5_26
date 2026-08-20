from datetime import datetime, timedelta

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)


with open("Sene.txt", "w") as file:
    file.write(yesterday.strftime("%d.%m.%Y %A") + "\n")
    file.write(today.strftime("%d.%m.%Y %A") + "\n")
    file.write(tomorrow.strftime("%d.%m.%Y %A") + "\n")

print("Sene.txt fayly doredildi!")