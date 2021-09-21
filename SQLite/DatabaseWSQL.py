import sqlite3

# Testing Ground for MySqlLite https://www.youtube.com/watch?v=byHcYRpMgI4

#Connect to database
conn = sqlite3.connect("customer.db") ## This will create a table or find one

#create a cursor
pointerCursor = conn.cursor()
#_----------------------------------------------------------------------------------
#Create a table ##m """""" = DocString

#pointerCursor.execute("""CREATE TABLE customers (
#    firstName  text,
#    lastName text,
#    email text                     #NOTE, This to create a table that doesn't exist. Because it was made already, we don't need to run it.
# ) 
#""")

#DataTYPES
#Null     - Does it exist?      
#INTERGER - Whole Numbers
#REAL     - 1.3 , 2.555
#TEXT     - Text dug
#BLOB     - "Store as it is?"

#_----------------------------------------------------------------------------------

#_----------------------------------------------------------------------------------
#many_customer_input = [
#
#    ('Wes'), ('Brown'), ('Wes@gmail.com')
#    
#    ]
#pointerCursor.executemany("INSERT INTO customers VALUES (?,?,?)", many_customer_input)
#_----------------------------------------------------------------------------------




#_----------------------------------------------------------------------------------
## How to insert one value at a time
#pointerCursor.execute("INSERT INTO customers VALUES('John', 'Smith', 'Test@gmail.com')") 
print("inserted Dummy Line")
#_----------------------------------------------------------------------------------


#_----------------------------------------------------------------------------------
#Query The Database
pointerCursor.execute("SELECT * FROM customers") 
#pointerCursor.fetchone()
#pointerCursor.fetchmany(3)
print(pointerCursor.fetchall())
#_----------------------------------------------------------------------------------




conn.commit() ##Need this to commit something to a database/Command

#Close our Connection - kinda similar to file openning
conn.close()