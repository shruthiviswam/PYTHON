def vowels(s):
    v = []
    c = []
    for i in s:
        if (i == "a")or (i == "e")or(i == "i")or(i == "o")or(i == "u"):
            v.append(i)
        else:
            c.append(i)
    print("vowels : ", v)
    print("constants : ", c)


s = input("Enter a string : ")
vowels(s)
