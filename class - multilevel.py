class Human:
    def __init__(self):
        self.name = input("Name : ")

    def properties(self):
        print("{} is the name of the person".format(self.name))


class Profession(Human):
    def __init__(self):
        Human.__init__(self)
        self.pro = input("Enter the Profession : ")

    def ach(self):
        print("{} is his profession".format(self.pro))


class Person(Profession):
    def __init__(self):
        Profession.__init__(self)

    def result(self):
        print("He is a good person")


p = Person()
p.properties()
p.ach()
p.result()
