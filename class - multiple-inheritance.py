class Human:
    def __init__(self, name):
        self.name = name

    def properties(self):
        print("{} is the name of the person".format(self.name))
        print("He can walk. He can talk.")


class Profession:
    def __init__(self, pro):
        self.pro = pro

    def ach(self):
        print("{} is his profession".format(self.pro))
        print("He is hard working.")


class Person(Human, Profession):
    def __init__(self, name, pro):
        Human.__init__(self, name)
        Profession.__init__(self, pro)

    def result(self):
        print("He is a good person")


p = Person("John", "musician")
p.properties()
p.ach()
p.result()
