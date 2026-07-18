import random 

colors = {"Red" : "Gyzyl",
        "Green" : "Yasyl",
        "Blue" : "Gok"
}

A = list(colors.keys())
print(random.choice(A))

A = list(colors.values())
print(random.choice(A))