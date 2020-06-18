a=int(input ("Enter the number : "))
r=0
b=a
while a!=0:
    m=a%10
    r=r*10+m
    a=a//10
print(r)
