class emp:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def _display(self):
        print("Name : {},{} years old.".format(self._name, self._age))


obj = emp("John", 10)
obj._display()
obj._age = 55
obj._display()
