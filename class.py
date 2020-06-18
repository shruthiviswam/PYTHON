class Student:
    course = "Python"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Your name is {} and your age is {}".format( self.name, self.age))

    def __del__(self):
        print("Destructor")


print(Student)
s1 = Student("John", 36)
s1.display()
s2 = Student("Maria", 25)
s2.display()
s2.course = "Angular"
print(s1.course)
print(s2.course)
