def unique(l1):
    l2=[]
    for i in l1:
        if i not in l2:
            l2.append(i)
    return l2

l1=[1,5,9,7,3,2,7,4,8,9,3,5,8]
print("The unique list is :",unique(l1))