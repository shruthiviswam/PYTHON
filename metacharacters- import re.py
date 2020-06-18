import re

txt = "The rain falls in Spain. 123 + * "
x = re.findall("[arn]", txt)
print(x)
if x:
    print("Yes, there is a match.")
else:
    print("no match")

x1 = re.findall("[0-9]", txt)
print(x1)

x2 = re.findall("[0-9][0-9][0-9]", txt)
print(x2)

x3 = re.findall("[+]",txt)
print(x3)

x4 = re.findall("[*]",txt)
print(x4)
