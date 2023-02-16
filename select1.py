import sqlite3
conn=sqlite3.connect('kims.db')
data1=conn.execute("select * from Details")
for row in data1:
    print("ID=",row[0])
    print("FIRSTNAME",row[1])
    print("LASTNAME",row[2])
    print("COURSE",row[3])
    print("SCHOOL",row[4])
    print("GENDER",row[5],"\n")
conn.close()
