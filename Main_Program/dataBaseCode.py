import sqlite3
from sqlite3.dbapi2 import IntegrityError, Timestamp
import Class
import sys


##@IgnacioFlores1500 - Test Commit - 11-19-2021 2:52AM
def createTables():
   con = sqlite3.connect("Database.db")
   #Cursor for the Database
   con.execute("PRAGMA foreign_keys = ON")
   pointer = con.cursor()
   #Creates Person Table
   
   pointer.execute(''' CREATE TABLE IF NOT EXISTS people
            (KeyID INTEGER PRIMARY KEY,
            FirstName TEXT NOT NULL,
            LastName TEXT NOT NULL,
            Suffix TEXT,
            ASUID INTEGER NOT NULL,
            RFID INTEGER NOT NULL,
            Email TEXT NOT NULL,
            PHONE INTERGER NOT NULL,
            CampusOFFCampus TEXT NOT NULL)
                ''')
     
        #Creates Professor Table
   pointer.execute(''' CREATE TABLE IF NOT EXISTS professors
        (ProfID INTEGER PRIMARY KEY,
        ContactID INTEGER NOT NULL,
        EditPrivages INTEGER NOT NULL,
        FOREIGN KEY(ContactID) REFERENCES people(KeyID))
        ''')
     
            #Creates Students Table
   pointer.execute(''' CREATE TABLE IF NOT EXISTS students
            (StudentID INTEGER PRIMARY KEY,
            ContactID INTEGER NOT NULL,
            COVID_Status TEXT NOT NULL,
            FOREIGN Key (ContactID) REFERENCES people (KeyID))
                ''')
     
            #Creates Courses Table  
   pointer.execute(''' CREATE TABLE IF NOT EXISTS courses
            (Course_ID INTEGER PRIMARY KEY,
            Course_Name TEXT NOT NULL,
            Building_Name TEXT NOT NULL,
            Room_Number INTEGER NOT NULL,
            roomClassSize INTEGER NOT NULL,
            professorID INTEGER NOT NULL,
            startDate INTEGER NOT NULL,
            endDate INTEGER NOT NULL,
            time INTERGER NOT NULL,
            FOREIGN Key (professorID) REFERENCES professors (ProfID)) 
                ''')
            #Creates Covid Table
#    pointer.execute(''' CREATE TABLE IF NOT EXISTS CovidDetails
#             (Student_ID INTEGER REFERENCES people(KeyID),
#             HasCovid INTEGER NOT NULL,
#             HadCovid INTEGER NOT NULL,
#             Date INTEGER NOT NULL)
#                 ''')
   
            #Creates activeClasses table, this tables should save all the classes that admin makes
   pointer.execute(''' CREATE TABLE IF NOT EXISTS activeClass
            (activeStudents INTEGER PRIMARY KEY,
            studentID INTEGER NOT NULL,
            courseID INTEGER NOT NULL,
            seatNumberX INTEGER NOT NULL,
            seatNumberY INTEGER NOT NULL,
            FOREIGN KEY (studentID) REFERENCES students (StudentID),
            FOREIGN KEY (courseID) REFERENCES courses (Course_ID))
       ''')
  
            #Creates Attendence
   pointer.execute(''' CREATE TABLE IF NOT EXISTS attendence
            (date TEXT PRIMARY KEY,
            courseID INTEGER NOT NULL,
            studentID INTEGER NOT NULL,
            attendence INTEGER NOT NULL,
            FOREIGN KEY (courseID) REFERENCES students (StudentID),
            FOREIGN KEY (courseID) REFERENCES courses (COURSE_ID))
       ''')
   

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
    
    def inputStudent():
        con = sqlite3.connect("Database.db")
        con.execute("PRAGMA foreign_keys = ON")
        #Cursor for the Database
        pointer = con.cursor()

        temp_contactID = None
        temp_covid = None

        while (temp_contactID == None):
            readFromDataBase.readPeopleTable()
            temp_contactID = input("Input contact ID")
        while (temp_covid == None):
            temp_covid = input("\"Covid\" or \"NoCovid\"")
        
        try: 
            pointer.execute("INSERT INTO students VALUES(Null, ?,?)", (temp_contactID, temp_covid))
            print("Inputed")
        except sqlite3.IntegrityError:
            print("Contact_ID Doesn't exist")        

        con.commit()
        con.close()
        

    def inputCourse(course):
        con = sqlite3.connect("Database.db")
        con.execute("PRAGMA foreign_keys = ON")
        #Cursor for the Database
        pointer = con.cursor()

        temp_ProfessorID = None


       
        while (temp_ProfessorID == None):
            readFromDataBase.readProfTable()
            print("Note, 1st Number is ProfID, 2nd Number is ContactID, 3rd Number is EditPrivileges")
            temp_ProfessorID = input("Insert perfessor ID ")
            ##temp_Edit_Priv = input("Do you want this Professor to have edit powers? (Yes or No) ")
            
        

        try: 
            pointer.execute("INSERT INTO courses VALUES(Null,?,?,?,?,?,?,?,?)", (course.courseName,course.buildingName,course.roomNumber,course.roomClassSize,temp_ProfessorID,course.startDate,course.endDate,course.time))
            print("Inputed")
        except sqlite3.IntegrityError:
            print("Missing or inValid Professor")
        con.commit()
        con.close()

    def inputActiveCourse(seatX,seatY):
        con = sqlite3.connect("Database.db")
        con.execute("PRAGMA foreign_keys = ON")
        #Cursor for the Database
        pointer = con.cursor()

        temp_studentID = None
        temp_courseID = None

        while (temp_studentID == None):
            readFromDataBase.readStudentTable()
            temp_studentID = input("Select a studentID ")
        while (temp_courseID == None):
            readFromDataBase.readCourseTable()
            temp_courseID = input("Select a courseID ")

        try:
            pointer.execute("INSERT INTO activeClass VALUES(Null, ?,?,?,?)", (temp_studentID,temp_courseID,seatX,seatY))
            print("Inputed")
        except sqlite3.IntegrityError:
            print("Missing or invalid, courseID or studentID")

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

    def readCourseTable():
        con = sqlite3.connect ("Database.db")
        con.execute("PRAGMA foreign_keys = ON")
        pointer = con.cursor()

        print("Course Table")
        print("------------------------------------")
        for x in pointer.execute("SELECT * FROM courses"):
            print(x)
        print("------------------------------------")

        con.commit()
        con.close() 

    def readStudentTable():
        con = sqlite3.connect ("Database.db")
        con.execute("PRAGMA foreign_keys = ON")
        pointer = con.cursor()

        print("Student Table")
        print("------------------------------------")
        for x in pointer.execute("SELECT * FROM students"):
            print(x)
        print("------------------------------------")

        con.commit()
        con.close()


    def readActiveCourseTable():
        con = sqlite3.connect ("Database.db")
        con.execute("PRAGMA foreign_keys = ON")
        pointer = con.cursor()


        print("ActiveCourse Table")
        print("------------------------------------")
        for x in pointer.execute("SELECT * FROM activeClass"):
            print(x)
        print("------------------------------------")

        con.commit()
        con.close()

    # def readCovidTable():
    #     con = sqlite3.connect ("Database.db")
    #     con.execute("PRAGMA foreign_keys = ON")
    #     pointer = con.cursor()

    #     print("Covid Table")
    #     print("------------------------------------")
    #     for x in pointer.execute("SELECT * FROM CovidDetails"):
    #         print(x)
    #     print("------------------------------------")

    #     con.commit()
    #     con.close() 


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
    
    def returnsFirstNameFromKeyID(KeyID):
        con = sqlite3.connect ("Database.db")
        con.execute("PRAGMA foreign_keys = ON")
        pointer = con.cursor()
        
        #for x in pointer.execute("SELECT KeyID FROM people WHERE RFID=(?)", (RFID,)):
        #   print(x)

        pointer.execute("SELECT FirstName FROM people WHERE KeyID=(?)", (KeyID,))
        return(pointer.fetchone())

        #for x in pointer.execute("SELECT * FROM (?)", ("people")):
        #    print(x)

        con.commit()
        con.close()

    def returnsContactIDFromStudentTableFromStudentTable(studentID):
        con = sqlite3.connect ("Database.db")
        con.execute("PRAGMA foreign_keys = ON")
        pointer = con.cursor()
        
        #for x in pointer.execute("SELECT KeyID FROM people WHERE RFID=(?)", (RFID,)):
        #   print(x)

        pointer.execute("SELECT ContactID FROM students WHERE studentID=(?)", (studentID,))
        return(pointer.fetchone())

        #for x in pointer.execute("SELECT * FROM (?)", ("people")):
        #    print(x)

        con.commit()
        con.close()

    def returnsCovidStatusFromStudentTableFromStudentTable(studentID):
        con = sqlite3.connect ("Database.db")
        con.execute("PRAGMA foreign_keys = ON")
        pointer = con.cursor()
        
        #for x in pointer.execute("SELECT KeyID FROM people WHERE RFID=(?)", (RFID,)):
        #   print(x)

        pointer.execute("SELECT COVID_Status FROM students WHERE studentID=(?)", (studentID,))
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

    def checkSeat(seati, seatj, course):
        con = sqlite3.connect ("Database.db")
        con.execute("PRAGMA foreign_keys = ON")
        pointer = con.cursor()

        #gravs the studentID from activeClass table. Need to find the contactId in student table later
        pointer.execute("SELECT studentID FROM activeClass WHERE courseID=(?) AND seatNumberX=(?) AND seatNumberY=(?)", (course, seati, seatj))
        studentID = pointer.fetchone()

        #print("First Step")
        #print(studentID[0])
        #Using that studentID, returns the contactID from the student table
        contactID = returnFromDataBase.returnsContactIDFromStudentTableFromStudentTable(studentID[0])

        
        #print("Second Step")
        #print(contactID[0])

        #Returns the firstName from contactID

        firstName = returnFromDataBase.returnsFirstNameFromKeyID(contactID[0])


        return(firstName[0])
    
    def checkSeatHealth(seati, seatj, course):
        con = sqlite3.connect ("Database.db")
        con.execute("PRAGMA foreign_keys = ON")
        pointer = con.cursor()

        #gravs the studentID from activeClass table. Need to find the contactId in student table later
        pointer.execute("SELECT studentID FROM activeClass WHERE courseID=(?) AND seatNumberX=(?) AND seatNumberY=(?)", (course, seati, seatj))
        studentID = pointer.fetchone()

        health = returnFromDataBase.returnsCovidStatusFromStudentTableFromStudentTable(studentID[0])
        return(health[0])
        ##StudentId is a number





