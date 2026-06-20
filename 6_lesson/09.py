print("""
< < < < Sohbets-TMCELL > > > >
1. Balance barlamak
2. Balance doldurmak
""")
balance = 31
hyzmat = int(input("Haysy hyzmat: "))
if hyzmat == 1:
    phone_number = int(input("+993 "))
    if 61000000 < phone_number < 65999999 or 71000000 < phone_number < 72999999:
        if 63696868 == phone_number:
            print(f"Salam Sohbet sen balans {balance}")
        else:
            print("bu senin nomurun dal")
elif hyzmat == 2:
    phone_number = int(input("+993 "))
    if 61000000 < phone_number < 65999999 or 71000000 < phone_number < 72999999:
        if 63696868 == phone_number:
            print(f"Salam Sohbet sen balans {balance}")
        else:
            print("Nadogry belgi")
        nace = int(input("Nace manat salmaly (1 - 500): "))
        if nace >= 1 and nace <= 500:
            print(f"Sizin balansynyz{nace} manat kopeldi\nSizin balansynyz {balance + nace} manat")
        else:
            print("Nadogry mocber")
    else:
        print("bu senin nomurun dal")
else:
    print("Hyzmat elyeterli dal")            