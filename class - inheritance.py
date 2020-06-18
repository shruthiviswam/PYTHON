class Fruits:
    def __init__(self):
        print("There are many fruits")

    def which(self, name):
        print("{} is a fruit".format(name))

    def sweet(self):
        print("It is sweet")


class Mango(Fruits):
    def __init__(self):
        Fruits().__init__()
        print("Its a mango")

    def which(self):
        print("Mango")

    def yellow(self):
        print("Mangoes are yellow")


f = Mango()
f.which()
f.sweet()
f.yellow()
