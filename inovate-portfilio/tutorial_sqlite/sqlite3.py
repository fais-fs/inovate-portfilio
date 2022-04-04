import sqlite3
conn = sqlite3.connect("mydata1.db") #connection created
#conn.cursor() #cursor created
def insertdata(task):
    query="INSERT INTO customer(c_name) VALUES('?');"
    conn.execute(query, (task))
    conn.close()

conn.execute('''CREATE TABLE IF NOT EXISTS customer(c_name text,c_lastname text,c_email text);''')
query="INSERT INTO customer(c_name) VALUES('FAZ');"
conn.execute(query)
conn.close()

query='SELECT *FROM customer;'
for rows in conn.execute(query):
    print(rows)
print("Database connected")
conn.close()