import mariadb
from datetime import datetime
import json
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="monty",
        password="123456",
        host="128.199.200.28",
        port=3306,
        database="testDB"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)


def checkOk(t = " ",description = " "):
    print("=====================================================")
    print(f"ok : {t}  / Description : {description}")
    print("=====================================================")
    

# mycursor  = conn.cursor()
# checkOk(1,"get cursor")

# # checkTable = mycursor.execute("SHOW TABLES")
# # print(checkTable)


# # mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
# # mycursor.execute("CREATE TABLE testNon (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), Datetime DATETIME(6) )")
# # mycursor.execute("CREATE TABLE testNon (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")
# mycursor.execute("CREATE TABLE testNon (memberId INT AUTO_INCREMENT PRIMARY KEY, id TEXT, name VARCHAR(255))")

# # checkOk(2,"Create Table")

# data1 = "name"
# val = "test"

# # mycursor.execute("INSERT INTO testNon (name) VALUES ('non')")
# # mycursor.execute(f"INSERT INTO testNon ({data1}) VALUES ('{val}')")

# # checkOk(3,"Add Data is Done!")

# conn.commit()
# # # print(mycursor.rowcount, "record inserted.")

# mycursor.close()
# conn.close()

# mycursor=conn.cursor(prepared=True)
# mycursor.execute("SELECT id FROM testNon")
# myresult = mycursor.fetchall()
# # for x in myresult:
# #     print(x)
# print(type(myresult))
# print(myresult)

# mycursor=conn.cursor(prepared=True)

# mycursor.execute("SELECT * FROM testNon")

# # Fetch all the rows of the result set
# result_set = mycursor.fetchall()

# # Convert the result set to a list of dictionaries
# rows = [dict(zip([col[0] for col in mycursor.description], row)) for row in result_set]

# # Convert the list of dictionaries to a JSON string
# json_string = json.dumps(rows)

# # Print the JSON string
# print(json_string)


cur  = conn.cursor()
  
  
query = f"UPDATE testNon SET id = 888888 WHERE name = 'non'"
  
cur.execute(query)
  
#To commit the changes
conn.commit() 
conn.close()
