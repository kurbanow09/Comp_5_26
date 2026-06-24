sagat = int(input("su wagt sagat nace (0-23)? "))

if sagat in range(0, 6):  
    print("su wagt Gije")
elif sagat in range(6, 13):  
    print("su wagt irden")
elif sagat in range(13, 19): 
    print("su wagt Oylan")
elif sagat in range(19, 24): 
    print("su wagt Agsam")
else:
    print("Nadogry sagat.")