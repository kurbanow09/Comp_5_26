print("---------- SYNAG BALLARY ----------")
print("Cykmak we netijani gormek ucin 'quit' diyip yazyn.")

Yykylanlar = 0
Gecenler = 0
while True:
    ballar = int(input("Okuwcynyn balyny girizin (0-100): "))
    if ballar < 100:
        print(f"->{ballar} bal: Gecdi")
    elif ballar < 50:
        print(f"->{ballar} bal: Yykyldy ")
    elif ballar == 111:
        print("=" * 30)
        print("SYNAGYN TOPARLAYYN NETIJESI")
        if Gecenler < 10:
        
        print(f"Toparda gecen okuwcy sany: {Gecenler}")
        print("=" * 30)