print("""
- - - Nahar Menu - - -
1-Manty 53 (TMT)
2-Dograma 60 (TMT)
3-Palow 50 (TMT)
""")

sayla = int(input("Sayla: "))
if sayla == 1:
    san = int(input("Sen nace sany manty aljak? "))
    print(f"Siz {san} sany manty aldynyz")
    print(f"Jemi {san * 53} TMT tolemeli")
elif sayla == 2:
    san = int(input("Sen nace sany Dograma aljak? "))
    print(f"Siz {san} sany Dograma aldynyz")
    print(f"Jemi {san * 60} TMT tolemeli")
elif sayla == 3:
    san = int(input("Sen nace sany Palow aljak? "))
    print(f"Siz {san} sany Palow aldynyz")
    print(f"Jemi {san * 50} TMT tolemeli")
else:
    print("Nadogry")