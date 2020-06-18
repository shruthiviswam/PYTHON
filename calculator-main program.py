import calculator

x = int(input("Enter a number : "))
y = int(input("Enter a number : "))
z = int(input("Enter a choice - 1.add 2.sub 3.mul 4.div : "))
print("The answer is : ")
if z == 1:
    calculator.add(x, y)
elif z == 2:
    calculator.sub(x, y)
elif z == 3:
    calculator.mul(x, y)
elif z == 4:
    calculator.div(x, y)
