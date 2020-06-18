class emp:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Age : ", self.age)


obj = emp("John", 10)
print("Name : ", obj.name)
obj.display()
