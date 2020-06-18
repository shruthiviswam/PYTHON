def check(s):
    u = 0
    l = 0
    for i in s:
        if (i.isupper()):
            u = u + 1
        elif (i.islower()):
            l = l + 1
    print("The number of uppercase is : ", u)
    print("The number of lowercase is : ", l)


s = "My Name Is Shruthi"
check(s)
