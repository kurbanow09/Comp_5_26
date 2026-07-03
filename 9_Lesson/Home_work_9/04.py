ort_jem = 0
toplam_talyp = 0
geçenler = 0
galanlar = 0

while True:
    baha = int(input("Student exam score: "))
    if baha == -1:
        break
    
    ort_jem += baha
    toplam_talyp += 1
    
    if baha >= 50: 
        geçenler += 1
    else:
        galanlar += 1

if toplam_talyp > 0:
    ortaça = ort_jem // toplam_talyp
    print(f"Quantity of Passed: {geçenler}")
    print(f"Quantity of Failed: {galanlar}")
    print(f"Average of Group: {ortaça}")