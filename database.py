import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="PYTHON_DATA"
)

mycursor = mydb.cursor()

# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#     print(x)

# mycursor.execute("CREATE TABLE class ( NAME VARCHAR(20), AGE VARCHAR(3), ID VARCHAR(10) PRIMARY KEY)")

# mycursor.execute("INSERT INTO class (NAME,AGE,ID) VALUES('ABHI',10,0001)")

# sql="INSERT INTO class (NAME, AGE, ID) VALUES (%s,%s,%s)"
# val=("RIYA","11","2")
# mycursor.execute(sql,val)

# sql="INSERT INTO class (NAME, AGE, ID) VALUES (%s,%s,%s)"
# val = [('MIYA', '9', '0003'), ('RAHUL', '8', '00005')]
# mycursor.executemany(sql,val)

# mydb.commit()

mycursor.execute("SELECT * from class")
cur = mycursor.fetchall()
for i in cur:
    print(i)