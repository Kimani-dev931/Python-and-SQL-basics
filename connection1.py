import sqlite3
conn=sqlite3.connect('kims.db')
print("opened db successfully")
conn.execute("INSERT INTO Details(ID,FIRSTNAME,LASTNAME,COURSE,SCHOOL,GENDER) VALUES(1,'Harrison','kimani','Fullstack','eMobilis','MALE')")
conn.execute("INSERT INTO Details(ID,FIRSTNAME,LASTNAME,COURSE,SCHOOL,GENDER) VALUES(2,'Felix','kipyegon','Javascript','eMobilis','MALE')")
conn.execute("INSERT INTO Details(ID,FIRSTNAME,LASTNAME,COURSE,SCHOOL,GENDER) VALUES(3,'Mary','Njeri','Cyber security','Modcom','FEMALE')")
conn.execute("INSERT INTO Details(ID,FIRSTNAME,LASTNAME,COURSE,SCHOOL,GENDER) VALUES(4,'Grace','wambui','Android','eMobilis','FEMALE')")
conn.execute("INSERT INTO Details(ID,FIRSTNAME,LASTNAME,COURSE,SCHOOL,GENDER) VALUES(5,'Peter','Ngugi','USSD','eMobilis','MALE')")
conn.execute("INSERT INTO Details(ID,FIRSTNAME,LASTNAME,COURSE,SCHOOL,GENDER) VALUES(6,'Brian','Macharia','Fullstack','eMobilis','MALE')")

conn.commit()
print("Records Added Successfully")
conn.close()
