import sqlite3
import Class


def createTables():
   con = sqlite3.connect("Database.db")
   #Cursor for the Database
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
      pointer.execute(''' CREATE TABLE professors
            (ProfID INTEGER REFERENCES people(KeyID), 
            EditPrivages INTEGER NOT NULL,
            Course_ID INTEGER REFERENCES courses(Course_ID))
                ''')

            #Creates Students Table
      pointer.execute(''' CREATE TABLE students
            (StudentID INTEGER REFERENCES people(KeyID),
            COVID_Status TEXT NOT NULL,
            Course_ID INTEGER NOT NULL)
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
   except:
        pass
        # Commit any changes into the Database.
   con.commit() 
        #Close our connection to the Database.
   con.close()


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

def readPeopleTable(tableName):
    con = sqlite3.connect ("Database.db")
    pointer = con.cursor()
    testTableName = "people"
    
    for x in pointer.execute("SELECT * FROM people"):
        print(x)

    #for x in pointer.execute("SELECT * FROM (?)", ("people")):
	#    print(x)

    con.commit()
    con.close()