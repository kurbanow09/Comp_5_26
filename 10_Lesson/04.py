phone = int(input("Phone number: +993"))
c = 0
while True:
    p = int(input("Please pay: "))
    if p == -1:
        print(f"{c} manats were tranferred to {phone}")
        break
    c += p
    print(f"You paid {c} manats")