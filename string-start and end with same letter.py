s = ["apple", "ball", "dad", "europe"]
c=0
d=0
for i in s:
    if len(i) >= 2 and i[0] == i[-1]:
        c = c + 1
    else:
        d = d + 1
print("The items with same start and end is : ", c)
print("The others are : ", d)
