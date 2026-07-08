b = []
a = ["dad", "only", "noon", "just", "eye", "like", "test"]
for i in a:
    if i[0] == i[-1]:
        b.append(i)
print(b)
print(f"Quantity: {len(b)}")