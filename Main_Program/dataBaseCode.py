import sqlite3
import Class


def createTables():
   con = sqlite3.connect("Database.db")
   #Cursor for the Database
   #con.execute("PRAGMA foreign_keys = 1")
   pointer = con.cursor()
   #Creates Person Table
   try:
      pointer.execute('''CREATE TABLE people
            (KeyID INTEGER PRIMARY KEY,
            FirstName TEXT NOT NULL,
            LastName TEXT NOT NULL,
            Suffix TEXT,
            ASUID INTEGER NOT NULL,
            RFID TEXT NOT NULL,
            Email TEXT NOT NULL,
            PHONE INTERGER NOT NULL,
            CampusOFFCampus TEXT NOT NULL)
                ''')

        #Creates Professor Table
      pointer.execute('''CREATE TABLE professors
        (ProfID INTEGER PRIMARY KEY,
        ContactID INTEGER NOT NULL,
        EditPrivages INTEGER NOT NULL,
        FOREIGN KEY (ContactID) REFERENCES people (KeyID))
        ''')

            #Creates Students Table
      pointer.execute(''' CREATE TABLE students
            (StudentID INTEGER PRIMARY KEY,
            ContactID INTEGER NOT NULL,
            COVID_Status TEXT NOT NULL,
            FOREIGN Key (ContactID) REFERENCES people (KeyID))
                ''')
            #Creates Courses Table  
      pointer.execute(''' CREATE TABLE courses
            (Course_ID INTEGER PRIMARY KEY,
            Course_Name TEXT NOT NULL,
            Building_Name TEXT NOT NULL,
            Room_Number INTEGER NOT NULL,
            Seats_In_Class INTEGER NOT NULL) 
                ''')
            #Creates Covid Table
      pointer.execute(''' CREATE TABLE covid_status
            (Student_ID INTEGER REFERENCES people(KeyID),
            Has_Covid TEXT NOT NULL,
            Had_Covid TEXT NOT NULL,
            Date INTEGER NOT NULL)
                ''')

        #CREATE ENROLLED TABLE
   except:
        print("ERROR")
        # Commit any changes into the Database.
   con.commit() 
        #Close our connection to the Database.
   con.close()

# def createProfessorTable():
#     con = sqlite3.connect("Database.db")
#     #Cursor for the Database
#     #con.execute("PRAGMA foreign_keys = 1")
#     pointer = con.cursor()
#     #Creates Person Table

#     pointer.execute('''CREATE TABLE professors
#         (ProfID INTEGER PRIMARY KEY,
#         ContactID INTEGER NOT NULL,
#         EditPrivages INTEGER NOT NULL,
#         FOREIGN KEY (ContactID) REFERENCES people (KeyID))
#         ''')
#         #Course_ID INTEGER REFERENCES courses(Course_ID)),
#     con.commit()
#     con.close()


def inputBasicInfoPeople(person):
    con = sqlite3.connect("Database.db")
    #Cursor for the Database
    pointer = con.cursor()
    #testInputName = people("Iggy", "Flowers", "None","999_999", "AB:CD:EF:GH", "111_111", "On_Campu")
    pointer.execute("INSERT INTO people VALUES(NULL,?,?,?,?,?,?,?,?)", (person.firstName, person.lastName, person.Suffix, person.ASUID, person.RFID, person.Email, person.Phone, person.CampusOFFCampus))
    print("INPUTED")
    con.commit()
    con.close()

def deleteBasicInfoPeople(IDNumber):
    con = sqlite3.connect("Database.db")
    #Cursor for the Database
    pointer = con.cursor()
    
    pointer.execute("DELETE FROM people WHERE KeyID=(?)", (IDNumber,))

    print("DELETE$D")
    con.commit()
    con.close()

def readPeopleTable():
    con = sqlite3.connect ("Database.db")
    pointer = con.cursor()
    testTableName = "people"
    
    for x in pointer.execute("SELECT * FROM people"):
        print(x)

    #for x in pointer.execute("SELECT * FROM (?)", ("people")):
	#    print(x)

    con.commit()
    con.close()

def readProfTable():
    con = sqlite3.connect ("Database.db")
    pointer = con.cursor()
    #testTableName = "people"
    
    for x in pointer.execute("SELECT * FROM professors"):
        print(x)

    #for x in pointer.execute("SELECT * FROM (?)", ("people")):
	#    print(x)

    con.commit()
    con.close()