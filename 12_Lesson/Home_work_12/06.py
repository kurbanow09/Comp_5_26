user_input = input("Enter the string: ")

words = user_input.split()

count = 0

for word in words:
    if "o" in word and "e" in word:
        count += 1

print(f"{count} words")