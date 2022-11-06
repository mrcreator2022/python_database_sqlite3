import sqlite3
conn = sqlite3.connect("sqlite.db")

print("Student id","Student name","Student class","Student fees")

#inner join
# data = conn.execute("SELECT f.st_id,s.st_name,s.st_class,f.fees_amount from fees as f inner join students as s on f.st_id=s.st_id ")

#left join
data = conn.execute("SELECT f.st_id,s.st_name,s.st_class,f.fees_amount from fees as f left join students as s on f.st_id=s.st_id ")

#right and full join not supported in sqlite3

for n in data:
    print(n[0] ,n[1] ,n[2], n[3])