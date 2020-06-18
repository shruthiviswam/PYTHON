import random
import math

print("The value of pi is ",math.pi)
print("choice : ",random.choice([1, 2, 3, 4, 5]))
print("randrange : ",random.randrange(10, 20, 5))
random.seed(2)
print("seed : ",random.random())
li = [1, 4, 2, 7, 6, 9]
random.shuffle(li)
for i in li:
    print(i)
print("uniform",random.uniform(5, 10))
