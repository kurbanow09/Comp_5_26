count = 0
for i in range(1, 1001):
    if i % 7 == 0 and i % 11 != 0:
        print(i)
        count = count + 1
    elif i % 7 == 0 and i % 11 == 0:
        i = i
    else:
        i = i
print("Bolunyan san")
print(count)