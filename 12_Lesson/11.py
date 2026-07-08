ballar = []
Students = int(input("How many students: "))
for i in range(1, Students + 1):
    score = int(input(f"{i}-student exam score: "))
    ballar.append(score)
ballar.sort()
print(ballar)
print(f"1-highest: {ballar[-1]}")
print(f"2-highest: {ballar[-2]}")
print(f"3-highest: {ballar[-3]}")