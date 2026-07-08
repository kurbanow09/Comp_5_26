user_input = input("Enter the string: ")

words = user_input.split()

for word in words:
    print(f"{word} - {len(word)}")