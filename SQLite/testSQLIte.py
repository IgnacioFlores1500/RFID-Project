import sqlite3
import Class
from Class import student

def createSqlTable():
	#---------------------------------------------------------
	con = sqlite3.connect("People_Class.db")
	#--------------------------------------------------------

	#Cursor for the Database
	pointer = con.cursor()

	#Creating a table
	try:
		pointer.execute('''	CREATE TABLE students
				(KeyID INTEGER,
				FirstName TEXT,
				LastName TEXT,
				ASUID INTEGER,
				CampusOFFCampus TEXT)
		''')
	except:
		print("Error")

	#HardCode a inputStatment
	#pointer.execute("INSERT INTO students VALUES(1, 'Iggy', 'Flores', 10000000, 'Campus' )")

	#Test input
	#pointer.execute("INSERT INTO students VALUES(?, ?, ?, ?,?)", (2, 'JP', 'Flores', 10000001, 'Off-Campus'))

	#print(pointer.fetchall())
	#for x in pointer.execute("SELECT * FROM students"):
	#	print(x)

	#Commit any changes into the Database.
	con.commit() 
	#Close our connection to the Database.
	con.close()



def inputNewRecord(studentObject):
	#---------------------------------------------------------
	con = sqlite3.connect("People_Class.db")
	#--------------------------------------------------------
	#Cursor for the Database
	pointer = con.cursor()

	pointer.execute("INSERT INTO students VALUES(?, ?, ?, ?,?)", (studentObject.key, studentObject.firstName, studentObject.lastName,studentObject.ASUID, studentObject.CampusOFFCampus))

	for x in pointer.execute("SELECT * FROM students"):
		print(x)

	#Commit any changes into the Database.
	con.commit() 
	#Close our connection to the Database.
	con.close()

def readEntireDataBase():
	con = sqlite3.connect("People_Class.db")
	pointer = con.cursor()

	for x in pointer.execute("SELECT * FROM students"):
		print(x)

	con.commit()
	con.close()