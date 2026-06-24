polo_jem = 0
otr_sany = 0

for i in range(1, 11):
    san = int(input(f"{i} - san yazyn: "))
    
    if san > 0:
        polo_jem += san 
    elif san < 0:
        otr_sany += 1  

print(f"Položitel sanlaryň jemi: {polo_jem}")
print(f"Otrisatel sanlaryň mukdary: {otr_sany}")