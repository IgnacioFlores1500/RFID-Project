import sqlite3
import Class
from Class import student


#Creates student.db table
def createSqlStudentTable():
	#---------------------------------------------------------
	con = sqlite3.connect("students.db")
	#con = sqlite3.connect("students.db")
	#--------------------------------------------------------
	#Cursor for the Database
	pointer = con.cursor()
	#Creating a table
	try:
		pointer.execute('''	CREATE TABLE students
				(KeyID INTEGER PRIMARY KEY,
				FirstName TEXT,
				LastName TEXT,
				ASUID INTEGER,
				CampusOFFCampus TEXT)
		''')
	except:
		print("Error")

	
	#Commit any changes into the Database.
	con.commit() 
	#Close our connection to the Database.
	con.close()

# def TESTINPUT():
# 	con = sqlite3.connect("People_Class.db")
# 	pointer = con.cursor()

# 	pointer.execute("INSERT INTO students VALUES(NULL,?,?,?,?)", ("JP", "Powers", 100002, "ONCAMPU"))

# 	con.commit()
# 	con.close()


#Using the studentObject [See Class.py for constructor], input the object into the database
def inputNewRecord(studentObject):
	#---------------------------------------------------------
	con = sqlite3.connect("students.db")
	#--------------------------------------------------------
	#Cursor for the Database
	pointer = con.cursor()

	#Insert studentObj into the database.
	pointer.execute("INSERT INTO students VALUES(NULL, ?, ?, ?,?)", ( studentObject.firstName, studentObject.lastName,studentObject.ASUID, studentObject.CampusOFFCampus))

	#Looks at table and prints that row
	#for x in pointer.execute("SELECT * FROM students"):
	#	print(x)

	#Commit any changes into the Database.
	con.commit() 
	#Close our connection to the Database.
	con.close()

def removeRecordFromID(KeyID):
	con = sqlite3.connect("students.db")
	pointer = con.cursor()

	pointer.execute("DELETE FROM students WHERE KeyID=(?)", (KeyID,))

	con.commit()
	con.close()
	#Remove readEntireDateBase Function later for production
	readEntireDataBase()


# Read the Entire function in the database
def readEntireDataBase():
	con = sqlite3.connect("students.db")
	pointer = con.cursor()

	for x in pointer.execute("SELECT * FROM students"):
		print(x)

	con.commit()
	con.close()

#Read the infomation from a given KeyID
def readIDFromDataBase(KeyID):
	con = sqlite3.connect("students.db")
	pointer = con.cursor()

	for x in pointer.execute("SELECT * FROM students WHERE KeyID=(?)", (KeyID,)):
		print(x)

	con.commit()
	con.close()

def getRecordViaFirstNameFromDataBase(Name):
	con = sqlite3.connect("students.db")
	pointer = con.cursor()

	splitName = Name.split('.')
	firstname = splitName[0]
	lastName = splitName[1]

	for x in pointer.execute("SELECT * FROM students WHERE FirstName=(?)", (firstname,)):
		print(x)
	
	con.commit()
	con.close()