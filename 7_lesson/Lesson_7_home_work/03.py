topar = int(input("Toparda nace okuwcy bar? "))

gecenler = 0
gechmedikler = 0
umumy_bal = 0

for i in range(1, topar + 1):
    bal = int(input(f"{i} - okuwcynyn synag bahasy: "))
    umumy_bal += bal
    
    if bal >= 50:
        gecenler += 1
    else:
        gechmedikler += 1

orta_baha = umumy_bal / topar


print(f"Synagdan gecen okuwcylaryn sany: {gecenler}")
print(f"Synagdan gecmedik okuwcylaryn sany: {gechmedikler}")
print(f"Toparyn ortaca bahasy: {orta_baha}")