import sqlite3
import Class
from Class import student

def createTables():
   con = sqlite3.connect("Database.db")
   #Cursor for the Database
   pointer = con.cursor()
   #Creates Person Table
   pointer.execute('''CREATE TABLE people
    (KeyID INTEGER PRIMARY KEY,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    Suffix TEXT,
    ASUID INTEGER NOT NULL,
    Email TEXT NOT NULL,
    PHONE INTERGER NOT NULL,
    CampusOFFCampus TEXT NOT NULL)
        ''')

    #Creates Professor Table
   pointer.execute(''' CREATE TABLE professors
    (ProfID INTEGER REFERENCES NOT NULL people(KeyID), 
    EditPrivages INTEGER NOT NULL,
    Course_ID INTEGER REFERENCES courses(Course_ID))
        ''')

    #Creates Students Table
   pointer.execute(''' CREATE TABLE students
    (StudentID INTEGER REFERENCES NOT NULL people(KeyID),
    COVID_Status TEXT NOT NULL,
    Course_ID INTEGER NOT NULL)
        ''')
    #Creates Courses Table  
   pointer.execute(''' CREATE TABLES courses
    (Course_ID INTEGER PRIMARY KEY,
    Course_Name TEXT NOT NULL,
    Building_Name TEXT NOT NULL,
    Room_Number INTEGER NOT NULL) 
        ''')
        # Commit any changes into the Database.
   con.commit() 
        #Close our connection to the Database.
   con.close()