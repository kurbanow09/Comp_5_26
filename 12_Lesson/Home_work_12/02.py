num_students = int(input("How many students: "))

best_name = ""
best_score = -1

for i in range(1, num_students + 1):
    name = input(f"{i}-student name: ")
    score = int(input(f"{i}-student exam score: "))
    
    if score > best_score:
        best_score = score
        best_name = name

print()
print(f"Exemplary student: {best_name}")
print(f"Exam score: {best_score}")