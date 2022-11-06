import sqlite3
conn = sqlite3.connect("sqlite.db")
st_id = input("Enter the student id: ")
conn.execute("DELETE from students where st_id="+st_id)
conn.commit()
conn.close()