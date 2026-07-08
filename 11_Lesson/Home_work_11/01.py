n = input("Lottery Ticket Number: ")
half = len(n) // 2
first_half = n[:half]
second_half = n[half:]

sum1 = 0
for x in first_half:
    sum1 += int(x)

sum2 = 0
for x in second_half:
    sum2 += int(x)

if sum1 == sum2:
    print("Lucky! You Won!")
else:
    print("Unlucky! You Lost!")