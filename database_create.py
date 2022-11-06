import sqlite3
conn = sqlite3.connect("sqlite.db")


conn.execute('''
          Create table fees (
              fees_id INTEGER PRIMARY KEY,
              st_id INT(11),
              fees_amount VARCHAR(50)
          )
 
''')

conn.close()