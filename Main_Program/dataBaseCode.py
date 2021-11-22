import sqlite3
import Class
import sys


##@IgnacioFlores1500 - Test Commit - 11-19-2021 2:52AM
def createTables():
   con = sqlite3.connect("Database.db")
   #Cursor for the Database
   con.execute("PRAGMA foreign_keys = ON")
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
        FOREIGN KEY(ContactID) REFERENCES people(KeyID))
        ''')

            #Creates Students Table
      pointer.execute(''' CREATE TABLE students
            (StudentID INTEGER PRIMARY KEY,
            ContactID INTEGER NOT NULL,
            COVID_Status TEXT NOT NULL,
            FOREIGN Key (ContactID) REFERENCES people (KeyID),
            FOREIGN Key (COVID_Status) REFERENCES Covid_Info (COVID_Status))
                ''')
            #Creates Courses Table  
      pointer.execute(''' CREATE TABLE courses
            (Course_ID INTEGER PRIMARY KEY,
            Course_Name TEXT NOT NULL,
            Building_Name TEXT NOT NULL,
            Room_Number INTEGER NOT NULL,
            roomClassSize INTEGER NOT NULL,
            professorID INTEGER NOT NULL,
            startDate INTEGER NOT NULL,
            endDate INTEGER NOT NULL,
            time INTERGER NOT NULL,
            FOREIGN Key (professorID) REFERENCES professor (ProfID)) 
                ''')
            #Creates Covid Table
      pointer.execute(''' CREATE TABLE CovidDetails
            (Student_ID INTEGER REFERENCES people(KeyID),
            HasCovid INTEGER NOT NULL,
            HadCovid INTEGER NOT NULL,
            Date INTEGER NOT NULL)
                ''')

            #Creates activeClasses table, this tables should save all the classes that admin makes
      pointer.execute(''' CREATE TABLE activeClass
            (activeStudents INTEGER PRIMARY KEY,
            studentID INTEGER NOT NULL,
            courseID INTEGER NOT NULL,
            seatNumber INTEGER NOT NULL,
            FOREIGN KEY (studentID) REFERENCES students (StudentID),
            FOREIGN KEY (courseID) REFERENCES courses (Course_ID))
       ''')
            #Creates Attendence
      pointer.execute(''' CREATE TABLE IF NOT EXIST attendence
            (date TEXT PRIMARY KEY,
            courseID INTEGER NOT NULL,
            studentID INTEGER NOT NULL,
            attendence INTEGER NOT NULL,
            FOREIGN KEY (courseID) REFERENCES students (StudentID),
            FOREIGN KEY (courseID REFERENCES courses (COURSE_ID))
       ''')
   except:
        print("Tables already made")
        # Commit any changes into the Database.
   con.commit() 
        #Close our connection to the Database.
   con.close()


#############################################################################################################################################
class inputDataBase:

    def inputBasicInfoPeople(person):
        con = sqlite3.connect("Database.db")
        con.execute("PRAGMA foreign_keys = ON")
        #Cursor for the Database
        pointer = con.cursor()
        #testInputName = people("Iggy", "Flowers", "None","999_999", "AB:CD:EF:GH", "111_111", "On_Campu")
        pointer.execute("INSERT INTO people VALUES(NULL,?,?,?,?,?,?,?,?)", (person.firstName, person.lastName, person.Suffix, person.ASUID, person.RFID, person.Email, person.Phone, person.CampusOFFCampus))
        print("INPUTED")
        con.commit()
        con.close()

    def inputProfessor():
        con = sqlite3.connect("Database.db")
        con.execute("PRAGMA foreign_keys = ON")
        #Cursor for the Database
        pointer = con.cursor()
        
        #TableLayOut:
        #ProfID PK
        #ContactID FK
        #EditPrivages INT 
        temp_ContactID = None
        temp_Edit_Priv = None
        temp2_Edit_Priv = None

        ##Fix this shit code later - 11-6-2021
        while (temp_Edit_Priv == None):
            readFromDataBase.readPeopleTable()
            temp_ContactID = input("Insert People ID ")
            temp_Edit_Priv = input("Do you want this Professor to have edit powers? (Yes or No) ")
            
        #1 = admin, 0 = normal
        if (temp_Edit_Priv == 'Yes'):
            temp2_Edit_Priv = 1
        elif (temp_Edit_Priv == "No"):
            temp2_Edit_Priv = 0
        else:
            print("ERROR")


        try: 
            pointer.execute("INSERT INTO professors VALUES(NULL,?,?)", (temp_ContactID,temp2_Edit_Priv))
            print("INPUTED")
        except sqlite3.IntegrityError:
            print("Contact_ID Doesn't exist")

        
        con.commit()
        con.close()
#############################################################################################################################################
class deleteFromDataBase:
    def deleteBasicInfoPeople(IDNumber):
        con = sqlite3.connect("Database.db")
        con.execute("PRAGMA foreign_keys = ON")
        #Cursor for the Database
        pointer = con.cursor()
        
        pointer.execute("DELETE FROM people WHERE KeyID=(?)", (IDNumber,))

        print("DELETE$D")
        con.commit()
        con.close()

    def deleteProfessor(IDNumber):
        con = sqlite3.connect("Database.db")
        con.execute("PRAGMA foreign_keys = ON")
        #Cursor for the Database
        pointer = con.cursor()
        
        pointer.execute("DELETE FROM professors WHERE ProfID=(?)", (IDNumber,))

        print("DELETE$D")
        con.commit()
        con.close()

#############################################################################################################################################
class readFromDataBase:
    def readPeopleTable():
        con = sqlite3.connect ("Database.db")
        con.execute("PRAGMA foreign_keys = ON")
        pointer = con.cursor()
        testTableName = "people"
        print("people table")
        print("------------------------------------")
        for x in pointer.execute("SELECT * FROM people"):
            print(x)
        print("------------------------------------")
        #for x in pointer.execute("SELECT * FROM (?)", ("people")):
        #    print(x)

        con.commit()
        con.close()

    def readProfTable():
        con = sqlite3.connect ("Database.db")
        con.execute("PRAGMA foreign_keys = ON")
        pointer = con.cursor()
        #testTableName = "people"
        
        print("prof table")
        print("------------------------------------")
        for x in pointer.execute("SELECT * FROM professors"):
            print(x)
        print("------------------------------------")
        #for x in pointer.execute("SELECT * FROM (?)", ("people")):
        #    print(x)

        con.commit()
        con.close()    
#############################################################################################################################################
class returnFromDataBase:
    def returnsKeyIDPeopleTableFromRFIDTag(RFID):
        con = sqlite3.connect ("Database.db")
        con.execute("PRAGMA foreign_keys = ON")
        pointer = con.cursor()
        
        #for x in pointer.execute("SELECT KeyID FROM people WHERE RFID=(?)", (RFID,)):
        #   print(x)

        pointer.execute("SELECT KeyID FROM people WHERE RFID=(?)", (RFID,))
        return(pointer.fetchone())

        #for x in pointer.execute("SELECT * FROM (?)", ("people")):
        #    print(x)

        con.commit()
        con.close() 


    def returnsInfomationFromPeopleTableFromFirstName(firstName):
        con = sqlite3.connect ("Database.db")
        con.execute("PRAGMA foreign_keys = ON")
        pointer = con.cursor()
        
        #for x in pointer.execute("SELECT KeyID FROM people WHERE RFID=(?)", (RFID,)):
        #   print(x)
        #print(firstName)

        ## And this is the named style:
        ##cur.execute("select * from lang where first_appeared=:year", {"year": 1972})
        ##print(cur.fetchall())

        pointer.execute("SELECT * FROM people WHERE FirstName = (?)", (firstName,))
        return(pointer.fetchone())  
        con.commit()
        con.close()   

    def returnsAdminStatusViaPersonID(peopleID):
        
        con = sqlite3.connect ("Database.db")
        con.execute("PRAGMA foreign_keys = ON")
        pointer = con.cursor()

        pointer.execute("SELECT EditPrivages FROM professors WHERE ContactID=(?)", (peopleID,))
        return(pointer.fetchone())
        
        con.commit()
        con.close()



