import sqlite3
conn = sqlite3.connect("sqlite.db")

data = conn.execute('''
update students set st_name="veer1" where st_id=1

''')

conn.commit()
conn.close()