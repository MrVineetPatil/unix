from sqlite3 import *
open('Hospital.db','w').close()
con=connect('Hospital.db')
cur=con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS Hospital(Hospital_ID int,Hospital_Name text,Bed_Count int)')
cur.execute('INSERT INTO Hospital VALUES(1,"MAYO CLINIC",200)')
cur.execute('INSERT INTO Hospital VALUES(2,"Cleveland Clinic",400)')
cur.execute('INSERT INTO Hospital VALUES(3,"Vineets Clinic",1000)')
cur.execute('INSERT INTO Hospital VALUES(4,"Sakshis Clinic",5000)')
con.commit()
print("HOSPITAL DB".center(31,'*'))
print("Hospital_ID\t\tHospital_Name\t\tBed_Count")
cur.execute('SELECT* FROM Hospital')
l=cur.fetchall()
for i in l:
    print(i[0],'\t\t\t',i[1].center(19),'\t\t\t',i[2],sep='')

print('Updating ID of Hospital ID 1 to 500')
cur.execute('UPDATE Hospital SET Bed_Count=500 WHERE Hospital_ID=1')
con.commit()
print("HOSPITAL DB".center(31,'*'))
print("Hospital_ID\t\tHospital_Name\t\tBed_Count")
cur.execute('SELECT* FROM Hospital')
l=cur.fetchall()
for i in l:
    print(i[0],'\t\t\t',i[1].center(19),'\t\t\t',i[2],sep='')

print('Delete hospital_id=3')
cur.execute('DELETE FROM Hospital WHERE Hospital_ID=3')
con.commit()
print("HOSPITAL DB".center(31,'*'))
print("Hospital_ID\t\tHospital_Name\t\tBed_Count")
cur.execute('SELECT* FROM Hospital')
l=cur.fetchall()
for i in l:
    print(i[0],'\t\t\t',i[1].center(19),'\t\t\t',i[2],sep='')