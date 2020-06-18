n = int(input("Enter the number : "))
s = 0
p = 0
for j in range(2, n):
    p = n % j
    if p == 0:
        s = 1
if s == 1:
    print("No, its not a prime number")
else:
    print("Yes! its a prime number")
