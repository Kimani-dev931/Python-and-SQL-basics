import sqlite3
conn=sqlite3.connect('kims.db')
conn.execute("CREATE TABLE Details"
             "(ID INT PRIMARY KEY NOT NULL,"
             "FIRSTNAME TEXT NOT NULL,"
             "LASTNAME TEXT NOT NULL,"
             "COURSE TEXT NOT NULL,"
             "SCHOOL TEXT NOT NULL,"
             "GENDER TEXT NOT NULL)")
print("table created successfully")
conn.close()