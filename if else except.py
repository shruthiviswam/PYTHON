x = int(input("Enter a number : "))
try:
    if x > 5:
        raise Exception("\nThe number is greater than 5.")
except Exception as e:
    print("An error has occured! ", e)
else:
    print("The number is lesser than 5.")

