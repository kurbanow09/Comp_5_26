user_input = input("Enter the string: ")

words = user_input.split()

for word in words:
    if "o" in word:
        print(word)