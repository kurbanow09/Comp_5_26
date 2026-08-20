import datetime
import random

bahasy = 0

def gos(idt, ady, hazirki_wagt):
    Harytlar.append(
        {
            "id": idt,
            "ady": ady,
            "baha": baha,
            "wagt": hazirki_wagt,
        }
    )
    print(f"--> '{ady}' Gosuldy!\n")


def sanawy_gor():
    print("\n" + "-" * 55)
    print("DUKAN SOWDA CEGI")
    print("-" * 55)
    if Harytlar:
        for o in Harytlar:
            print(
                f" ID: {o['id']} |{o['ady']} |{o['wagt']} --> {baha}"
            )

            print(f"JEMI BAHASY {bahasy}")
    else:
        print("Hic hili haryt girizilmedi.")


print("-" * 55)
print("Cykmak ucin 'stop' yaz.")

Harytlar = []

while True:
        ady = input("Harydyn ady: ")
        if ady.lower() == "stop":
            break
        baha = int(input("Harydyn Bahasy: "))
        hazirki_wagt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        idt = random.randint(1000, 9999)
        bahasy += baha
        gos(idt, ady, hazirki_wagt,)


sanawy_gor()