print("Welcome to SmartMarket!")

yerli = {
        "alma": {"category": "TMT", "price": 15},
        "Corek": {"category": "TMT", "price": 3},
        "Suyt": {"category": "TMT", "price": 12}
    }

for i, j in yerli.items():
    print(f"Yerli harytlar: {i} ({j['category'].capitalize()}):")

yersiz = {
        "Noutbuk": {"category": "USD", "price": 800},
        "Telefom": {"category": "EUR", "price": 500}
}

for i, j in yersiz.items():
    print(f"Dasary yurt harytlar: {i} ({j['category'].capitalize()}):")