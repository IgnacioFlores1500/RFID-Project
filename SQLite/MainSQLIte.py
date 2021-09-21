import sqlite3


#---------------------------------------------------------
con = sqlite3.connect(":memory:")
#--------------------------------------------------------

#Cursor for the Database
pointer = con.cursor()

#Creating a table

pointer.execute('''	CREATE TABLE students
			(KeyID INTEGER, FirstName TEXT, LastName TEXT, ASUID INTEGER, CampusOFFCampus TEXT)
''')

pointer.execute("INSERT INTO students VALUES(1, 'Iggy', 'Flores', 10000000, 'Campus' )")


#Commit any changes into the Database.
con.commit() 
#Close our connection to the Database.
con.close()



