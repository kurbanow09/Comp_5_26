geçenler = 0
galanlar = 0
toplam_talyp = 0

while True:
    baha = int(input("Student exam score: "))
    if baha == -1:
        break
        
    toplam_talyp += 1
    if baha >= 50:
       
        geçenler += 1
    else:
        galanlar += 1

if toplam_talyp > 0:
    geçen_göterim = int((geçenler / toplam_talyp) * 100)
    galan_göterim = int((galanlar / toplam_talyp) * 100)
    
    print(f"Quantity of Passed: {geçenler}")
    print(f"Quantity of Failed: {galanlar}")
    print(f"Percent of Passed: {geçen_göterim} %")
    print(f"Percent of Failed: {galan_göterim} %")