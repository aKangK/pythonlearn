import sqlite3 as sq3
conn=sq3.connect("First.db")
#==================================================
cur=conn.cursor()
cur.execute('select * from T_fish')
for row in cur.fetchall():
    print(row)


#==================================================
conn.close