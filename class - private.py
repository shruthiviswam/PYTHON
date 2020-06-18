class emp:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def display(self):
        print("Name : {},{} years old.".format(self.__name, self.__age))


obj = emp("John", 10)
obj.display()
obj.__age = 55
print(obj.__age)
obj.display()
obj._emp__age=22
obj.display()