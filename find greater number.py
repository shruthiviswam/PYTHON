a=input("Enter a: ")
b=input("Enter b: ")
print("value of a is {} and value of b is {}".format(a,b))
if a>b:
    print("{} is greater than {}".format(a,b))
elif b>a:
    print("{} is greater than {}".format(b,a))
else:
    print("They are equal")