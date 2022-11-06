import sqlite3
conn = sqlite3.connect("sqlite.db")

data = conn.execute("SELECT * from students limit 0,2")
print("Student id","Student name","Student class","Student email")
for n in data:
    print(n[0],n[1],n[2],n[3])