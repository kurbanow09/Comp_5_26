a = []
b = []
while True:
    word = input("Enter the word: ")
    if word == "0":
        break
    elif word[0] == word[-1]:
        a.append(word)
    b.append(word)
print(f"girizilen sozler: {','.join(b)}")
print(f"Netije: {a}")