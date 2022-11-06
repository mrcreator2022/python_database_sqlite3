import sqlite3
conn = sqlite3.connect("sqlite.db")
st_name = input("Enter student name: ")
st_class = input("Enter student class: ")


#data = conn.execute("SELECT * from students where st_name ='"+st_name+"' ")
#data = conn.execute("SELECT * from students where st_name like '%"+st_name+"%' and st_class like '%"+st_class+"%' ")
data = conn.execute("SELECT * from students where st_name like '%"+st_name+"%' or st_class like '%"+st_class+"%' ")
print("Student id","Student name","Student class","Student email")
for n in data:
    print(n[0],n[1],n[2],n[3])