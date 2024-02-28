import sqlite3
## conection 
connection=sqlite3.connect("student1.db")

##creating a cursor resposible for retrieving and creating table
cursor = connection.cursor()
table_info = """
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25), MARKS INT)

"""
cursor.execute(table_info)


##CMD For inserting records
cursor.execute('''INSERT INTO STUDENT VALUES ('Krish', 'Data Science', 'A',90)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Darius', 'Data Science', 'B',100)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Sudhanshu', 'Devops', 'C',86)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Vikash', 'Data Science', 'C',50)''') 

# Display data inserted 
print("Data Inserted in the table: ") 
data=cursor.execute('''SELECT * FROM STUDENT''') 
for row in data: 
    print(row) 
  
# Commit your changes in the database     
connection.commit()
# Closing the connection 
connection.close()