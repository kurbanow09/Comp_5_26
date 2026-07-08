num_students = int(input("How many students: "))

scores = []
for i in range(1, num_students + 1):
    score = int(input(f"{i}-student exam score: "))
    scores = scores + [score]

highest = scores[0]
lowest = scores[0]
total = 0

for score in scores:
    if score > highest:
        highest = score
    if score < lowest:
        lowest = score
    total = total + score

average = int(total / num_students)

print()
print(f"Highest score: {highest}")
print(f"Lowest score: {lowest}")
print(f"Average of group: {average}")