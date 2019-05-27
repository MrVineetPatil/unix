from sqlite3 import *
open('Employee.db','w').close()
con=connect('Employee.db')
cur=con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS Employee (Name TEXT ,Salary INTEGER)')
cur.execute("INSERT INTO Employee VALUES('A',20000)")
cur.execute("INSERT INTO Employee VALUES('B',30000)")
cur.execute("INSERT INTO Employee VALUES('C',50000)")
cur.execute("INSERT INTO Employee VALUES('D',60000)")
cur.execute("INSERT INTO Employee VALUES('E',70000)")
cur.execute("INSERT INTO Employee VALUES('F',80000)")
con.commit()
cur.execute('SELECT* FROM Employee WHERE Salary>50000')
l=cur.fetchall()
print("NAME\tSALARY")
for i in l:
    print(i[0]+'\t\t'+str(i[1]))