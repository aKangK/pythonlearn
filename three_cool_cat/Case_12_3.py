import sqlite3 as sq3
conn=sq3.connect("First.db")
#==================================================
cur=conn.cursor()
cur.execute('Create table T_fish(date text,name text,nums int,price real,Explain text)')
cur.execute("insert into T_fish Values('2018-3-28','黑鱼',10,28.3,'Tom')")
cur.execute("insert into T_fish Values('2018-3-29','鲤鱼',17,10.3,'John')")
cur.execute("insert into T_fish Values('2018-3-30','鲑鱼',9,9.2,'Tim')")
conn.commit()
cur.execute("select * from T_fish")
for row in cur.fetchall():
    print(row)
cur.execute("delete from T_fish where nums=10")
conn.commit()
cur.execute('select * from T_fish')
for row in cur.fetchall():
    print(row)
    
#==================================================
conn.close