import hashlib

password = input("enter the password : ")
salt='@@@'+password
obj = hashlib.md5(salt.encode())
encryption = obj.hexdigest()
print(obj)
print(encryption)

password1 = b'password123'
salt1=b'@@@'+password1
obj1 = hashlib.sha1(salt1)
enc = obj1.hexdigest()
print(obj1)
print(enc)
