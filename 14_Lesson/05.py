ishgarler={"Turkmenistan" : {"capital" : "Ashgabat",
"Currency" : "Manat (TMT)",
 "Population" : " 7 Million"},

"Uzbek" : {"capital" : "Tashkent",
"currency" : "Som (UZS)",
"population" : "37 Million"},


"Kazakhistan" : {"capital" : "astana",
"currency" : "tnege (KZT)",
"population" : "20 million"},
}

kassa = 0
operation = ""

while operation != 'quit':
    print("1. TURKMENISTAN")
    print("2. uzbek")
    print("3. kazakhistan")


    operation = input('Name etmeli (san girizin):')

    if operation == '1':
        print(ishgarler["Turkmenistan"])
    elif    operation == '2':
        print(ishgarler["Uzbek"])
    elif    operation == '3':
        print(ishgarler["Kazakhistan"])
