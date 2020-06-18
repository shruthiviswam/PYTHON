#paliandrome
x=int(input ("Enter the number : "))
rev=0
y=x
while x!=0:
    rem=x%10
    rev=rev*10+rem
    x=x//10
if (rev==y):
    print("Its paliandrome!")
else:
    print("Not paliandrome.")