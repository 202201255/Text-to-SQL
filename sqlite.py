import sqlite3

# connect to SQLite
connection = sqlite3.connect("student.db")

# create a cursor object
cursor = connection.cursor()

# Drop the table if it exists (to start fresh)
cursor.execute("DROP TABLE IF EXISTS STUDENT")

# create table
table_info = """
  CREATE TABLE STUDENT(NAME VARCHAR(25), PROGRAM VARCHAR(25), SECTION VARCHAR(25))
"""
cursor.execute(table_info)


# insert records
cursor.execute("INSERT INTO STUDENT VALUES('Raj','Computer science','A')")
cursor.execute("INSERT INTO STUDENT VALUES('Rahul','Data science','B')")
cursor.execute("INSERT INTO STUDENT VALUES('Ravi','Cloud Computing','C')")
cursor.execute("INSERT INTO STUDENT VALUES('Rohit','Data science','A')")
cursor.execute("INSERT INTO STUDENT VALUES('Rajesh','Data science','B')")
cursor.execute("INSERT INTO STUDENT VALUES('Rajat','DEVOPS','C')")



# display records
print("the inserted records are:")
data = cursor.execute("SELECT * FROM STUDENT")

for row in data:
    print(row)

connection.commit()
connection.close()