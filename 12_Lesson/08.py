b = []
a ={"fun", "only", "day", "just", "end", "like"}
for i in a:
    if len(i) == 4:
        b.append(i)
print(b)
print(f"Quantity: {len(b)}")