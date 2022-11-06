import sqlite3
conn = sqlite3.connect("sqlite.db")

# ins = '''
#        insert into students (st_name,st_class,st_email) VALUES ('Veer','12th','veer@gmail.com')
# '''

ins = '''
       insert into fees (st_id,fees_amount) VALUES (3,3000)
'''
conn.execute(ins)
conn.commit()
conn.close()
