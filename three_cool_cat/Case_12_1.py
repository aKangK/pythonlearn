import sqlite3 as sq3
conn=sq3.connect("First.db")
#==================================================
cur=conn.cursor()
cur.execute('Create table T_fish(date text,name text,nums int,price real,Explain text)')
cur.execute("insert into T_fish Values('2018-3-28','黑鱼',10,28.3,'Tom')")
conn.commit()


#==================================================
conn.close