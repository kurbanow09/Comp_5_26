import datetime
import random


def okuwcy_gos(okuwcy_id, ady, yasy, ortaca_baha, hazirki_wagt):
    okuwcylar.append(
        {
            "id": okuwcy_id,
            "ady": ady,
            "yasy": yasy,
            "baha": ortaca_baha,
            "wagt": hazirki_wagt,
        }
    )
    print("-->Gosuldy!\n")


def sanawy_gor():
    print("\n" + "-" * 55)
    print("GIRIZILEN OKUWCYLARYN SANAWY")
    print("-" * 55)
    if okuwcylar:
        for o in okuwcylar:
            print(
                f"ID: {o['id']} | Ady: {o['ady']} | Yasy: {o['yasy']} | Baha: {o['baha']} | Gosulan wagty: {o['wagt']}"
            )
        gunun_okuwcysy = random.choice(okuwcylar)
        print("-" * 55)
        print(
            f"🌟 Gunun Okuwcysy (Random): {gunun_okuwcysy['ady']} (ID: {gunun_okuwcysy['id']})"
        )
    else:
        print("Hic hili okuwcy girizilmedi.")


print("-" * 55)
print("Cykmak ucin 'stop' yaz.")

okuwcylar = []

while True:
    ady = input("Okuwcynyn ady: ")
    if ady.lower() == "stop":
        break
    yasy = input("Okuwcynyn yasy: ")
    hazirki_wagt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    okuwcy_id = random.randint(1000, 9999)
    ortaca_baha = random.randint(70, 100)
    okuwcy_gos(okuwcy_id, ady, yasy, ortaca_baha, hazirki_wagt)

sanawy_gor()