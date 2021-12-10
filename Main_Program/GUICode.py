#This program is designed to display information from a sql data base and set a "classroom" with students
#The program is specifically designed for the RFID scanner used in software engineering fall 2021
#JohnPaul Flores is the sole author of this code as of 10/21/21
#Software Engineering
#JohnPaul Flores CID: 81340848
#Last Edited: Date 10/21/21





##
# To use the "generic" widgets
import tkinter as tk
# To use the stylized, "look-and-feel" widgets
from tkinter import Entry, ttk
# To display any error or warnings for mistakes, and to make sure the user wants to enter the info
from tkinter import messagebox
# sublibrary to ask for any info the program needs from the user 
from tkinter import simpledialog
from tkinter.constants import BEVEL, CENTER, DISABLED, END
from typing import Counter
# sublibrary to 


##Allows the GUI to know when a login was made
import time

##Imports a function from database file to return if a personID has edit_prilvages
from dataBaseCode import returnFromDataBase
## imports the people class from Class.py to import data
from Class import people
##Imprts a functions that allows to import users into database
from dataBaseCode import inputDataBase
##Imports readFunctions that allows to use read the database using functions
from dataBaseCode import readFromDataBase
##Imports function to update to database
from dataBaseCode import updateToDataBase




##comment if no RFID

# import RPi.GPIO as GPIO
# from mfrc522 import SimpleMFRC522

#reader = SimpleMFRC522()

TrueUser = False
TruePassword = False
CurrentFailedAttempt = False
hasBeenCreated = False
recentClassSize = 0
seats = {}
adminFields = {}
CurrentLogin = ""



def main():
    #creating program
    program = RFIDDisplay()
    #starting event loop
    program.window.mainloop()

class RFIDDisplay:

    def __init__(self):
        #Making the application window
        self.window = tk.Tk()

        ##program Dimenisons
        windowWidgth = 1200
        windowHight = 700

        ##screen dimension
        screenWidth = self.window.winfo_screenwidth()
        screenHight = self.window.winfo_screenheight()

        ##center points
        centerX = int(screenWidth/2 - windowWidgth /2)
        centerY = int(screenHight/2 - windowHight /2)

        #gemotry


        self.window.geometry(f'{windowWidgth}x{windowHight}+{centerX}+{centerY}')
        #self.window.resizable(0,0)
        
        ##Creates the size of the application
        ##self.canvas = tk.Canvas(self.window, width=900, height=600)
        ##self.window.geometry = ('900x900')
        ##Creates the number of columns and rows before hand
        #self.window.resizable(0,0)
        ##self.canvas.grid(column=15, rows=20)
        
        #self.window.columnconfigure(0, weight=1)
        #self.window.rowconfigure(0,weight=1)
        
        # self.canvas.columnconfigure(6, weight=1)
        # self.canvas.columnconfigure(0, weight=1)

        self.create_widgets()
        #self.RFIDENTRY()
        #self.welcomScreen()
    

    # def RFIDENTRY(self):
    #     import time

    #     import RPi.GPIO as GPIO
    #     from mfrc522 import SimpleMFRC522

    #     reader = SimpleMFRC522()

    #     print("Scan Card")
    #     try:
    #         while True:
    #             rfid = None
    #             text = None
    #             rfid, text = reader.read()
                
    #             if (returnFromDataBase.returnsKeyIDPeopleTableFromRFIDTag != None):
    #                 self.entry(rfid)
    #                 print(rfid)
    #                 #print(rfid)
    #                 GPIO.cleanup()
    #                 break
    #             time.sleep(2)

    #     finally:
    #         print("TEST")
    #         GPIO.cleanup()



        
    def entry(self,rfid):
        temptumble1 = returnFromDataBase.returnsKeyIDPeopleTableFromRFIDTag(rfid)
        keyid = temptumble1[0]
        tempTumble = returnFromDataBase.returnsFirstNameFromKeyID(keyid)
        #print(tempTumble)
        #print("DEBUYG")
        user = tempTumble[0]
        print(user)
        TrueUser = True
        TruePassword = True
        self.show_admin_powers()
        self.recentUser = ttk.Label(self.window, text =  "Current User: " + user, font=3)
        self.recentUser.grid(row=2, column=0,sticky=tk.W, columnspan=5)
        epochSeconds = time.time()
        localTime = time.ctime(epochSeconds)
        self.loginTime = ttk.Label(self.window, text = "Session started " + localTime, font=3)
        self.loginTime.grid(row=3, column=0,sticky=tk.W, columnspan=5)
        
        ##self.RFIMessage.bind("<Return>", self.create_widgets)
        ##self.canvas.columnconfigure(6, weight=1)
     
    #isAdmin sends what the user input for logging in. This will be the log in page for the UI and
    #if the username and password are correct then it will provide access to the classroom state and 
    #modifying priveliges to the classroom as well
    def isAdminFromFirstName(self, event, firstName):
        #def isAdmin(self, event, accounts):
        #taking data entered into the entry and chcecking it for authentification
        
        print("hello")
        ##idk what this actually does -iggy
        enteredName = self.my_entry.get()

        CurrentLogin = self.name_entry.get()
        
        print(enteredName)
        ##Grabs tuple of people data based from the user 
        resultingInfo = returnFromDataBase.returnsInfomationFromPeopleTableFromFirstName(firstName)

        ## 
        if resultingInfo:
            grabbedPersonID = resultingInfo[0]
        else:
            return False

        ##Using the KeyID from the people table, we look returnsAdmin...Function 
        ##that looks at the EditPrivages
        Status = returnFromDataBase.returnsAdminStatusViaPersonID(grabbedPersonID) ##This should be either a 1 or 0

        ##Test that Status
        if (Status == 1):
            print("TRUETEST")
            TrueUser = True
            TruePassword = True
            self.create_widgets()
            return True
        else:
            print("FALSETEST")
            self.create_widgets()
            return False

    #validPassword takes what the user entered into the passwd box and sees if the password 
    #and username match the ones in the data base #if the valid long in is false, delete all of admin
    def validLogin (self, event):
        passwd = self.password_entry.get()
        user = self.name_entry.get()
        
        ##Leave Password true atm
        TruePassword = True
        firstNameDBFinal = ()

        ##This returns a tuple of the people table from the firstName you put in user = self.name_entry.get()
        firstNameFromDatasBase = returnFromDataBase.returnsInfomationFromPeopleTableFromFirstName(user)
        ##lastNameFromDataBase =
        ##If the tuple does exist, (aka there is someone called whatever the user puts)
        ##Grab the firstname of the tuple

        if firstNameFromDatasBase:
            firstNameDBFinal = firstNameFromDatasBase[1]
            ##Kinda not needed, but it's like a second check
            ##Checsk to see the resulted firstName is the same as the user inputed
            if (firstNameDBFinal == user):
                    TrueUser = True
            else:
                TrueUser = False
           
        ## if there is no tuple of the user,h the person doesn't exist in the database
        else:
            TrueUser = False

        if TrueUser == False or TruePassword == False:
            self.display = ttk.Label(self.window, text="Invalid Login LOL")
            self.display.grid(row=4, column=0, sticky=tk.W, pady=5)
            self.classroom.destroy()
            self.firstNameEntry.destroy()
            self.lastNameEntry.destroy()
            self.suffixEntry.destroy()
            self.AngeloIDEntry.destroy()
            self.tagEntry.destroy()
            self.emailEntry.destroy()
            self.HousingStatusEntry.destroy()
            self.insert_Record_Button.destroy()

            if recentClassSize != 0:
                for i in range(recentClassSize):
                    for j in range(3, recentClassSize + 3):
                        seats[(i, j + 3)].destroy()
                CurrentFailedAttempt = True

            #if the login isnt valid, show no one is logged in
            self.recentUser.destroy()
            self.recentUser = ttk.Label(self.window, text = "No one is currently logged in")
            self.recentUser.grid(row=6, column=0,sticky=tk.W, pady=20)
        else:
            #If Above passes, show the create classroom -iggy
            self.show_admin_powers()
            

            #if the login is valid, show who is logged in
            self.recentUser.destroy()
            self.recentUser = ttk.Label(self.window, text =  "Current User: " + user, font=3)
            self.recentUser.grid(row=2, column=0,sticky=tk.W, columnspan=5)


            ##Logged in time: When the user logged in
            epochSeconds = time.time()
            localTime = time.ctime(epochSeconds)
            self.loginTime = ttk.Label(self.window, text = "Session started " + localTime, font=3)
            self.loginTime.grid(row=3, column=0,sticky=tk.W, columnspan=5) 
            
    #show admin powers is to enable the ability to change a class and or roster
    def show_admin_powers(self):
        if CurrentFailedAttempt == True:
            self.display.delete(0, END)
        
        ##Deletes the login entries. Could possible change later after implementing the RFID scanner
        self.name_entry.destroy()
        self.password_entry.destroy()
        self.login_button.destroy()
        ##un comment this if using creatwigets


        ##show_admin_button shows the buttons that allows professor to edit and add classrooms/students/professors, ect
        ##SignoutButton, is created to allow the professor to signout of their session. This might be a way to allow students to once again sign-in
        self.show_admin_buttons()
        self.SignOutButton()
        #self.createHomeButton()
        
        ## runs a self.function that creates the fields to input people into the data. 
        #self.entrySection()
        #self.create_widgets()

    ##This function creates the button used for the admin status. 
    def show_admin_buttons(self):
        ##Input person Button
        self.entryButtonSection = tk.Button(self.window,width=20, text = "Create person")
        self.entryButtonSection.grid(row=8, column=0,sticky=tk.W, pady=5)
        self.entryButtonSection.bind("<Button>", self.createStudentsEntrySection)

        ##Create Classroom button
        self.createClassRoom = tk.Button(self.window,width=20, text = "Create Classroom")
        self.createClassRoom.grid(row=8, column=1,sticky=tk.W, pady=5)
        self.createClassRoom.bind("<Button>", self.createClassroomEntrySection)

        self.showClass = tk.Button(self.window, width=20, text = "Show Classroom")
        self.showClass.grid(row=8, column=2,sticky=tk.W, pady=5)
        self.showClass.bind("<Button>", self.createClassEntry)

        self.editPersonButton = tk.Button(self.window,width=20, text = "Edit person")
        self.editPersonButton.grid(row=9, column=0,sticky=tk.W, pady=5)
        self.editPersonButton.bind("<Button>", self.editStudentsEntrySection)

        self.editClassroomButton = tk.Button(self.window,width=20, text = "Edit Classroom")
        self.editClassroomButton.grid(row=9, column=1,sticky=tk.W, pady=5)
        self.editClassroomButton.bind("<Button>", self.createClassEntry)

        self.deletePersonButton = tk.Button(self.window,width=20, text = "Delete person")
        self.deletePersonButton.grid(row=9, column=2,sticky=tk.W, pady=5)
        self.deletePersonButton.bind("<Button>", self.deleteStudentEntrySection)
        try:
            self.homeButton.destroy()
        except:
            pass

    ##Creats the Entry for the classroom after the button is clicked
    def createClassEntry(self, event):

        self.destroyAllPossibleAdminFields_Buttons()
        
        self.classroom = ttk.Entry(self.window, width=50)
        self.classroom.grid(row=7, column=0, sticky=tk.W, pady=5)
        self.classroom.insert(tk.END, "Enter the class size you want (Perfect Square)")
        self.classroom.bind("<Return>", self.create_class)  

        self.createHomeButton()  
    
    #Create class is meant to make the classroom on the UI by making empty seats.
    def create_class(self, event):
        global seats
        global recentClassSize
        hasBeenCreated = True
        global classSize


        course = self.classroom.get()
        ###I assume to type_cast classSize from string to integer
        course = int(course)

        if recentClassSize != 0:
            for i in range(recentClassSize):
                for j in range(5, recentClassSize + 5):
                    try:
                        seats[(i, j + 5)].destroy()
                    except:
                        pass


        #for i in range(RecentClassSize):
            #for j in range(2, RecentClassSize + 2):
                #self.b = ttk.Label(self.window, text="")
                #self.b.grid(row=i, column=j, pady=5)
        for i in range(course):
            for j in range(5, course + 5):
                b = ttk.Label(self.window, text=returnFromDataBase.checkSeat(i, j, course) + returnFromDataBase.checkSeatHealth(i, j, course))
                b.grid(row=i, column=j, pady=5)
                seats[(i, j + 5)] = b
        
        recentClassSize = course
        

        ##destroys the entry field
        self.destroyAllPossibleAdminFields_Buttons()
        self.classroom.destroy()

        ##Copy from create_widgets Function. This is a crappy fix to fix 
        ## A bug when creating classrooms
        self.title = ttk.Label(self.window, text="RFID COVID-19 Tracker")
        self.title.config(anchor=CENTER)
        self.title.grid(row=0, column=0,columnspan=5)
       
        ##Replaces the fields location witht the admin buttons
        self.show_admin_buttons()

    #this function is connected to the update database button specifically for 
    #the time being
    def addToDatabase(self, event):


        ##Goodate is a value to check if the data in the entry is correct.
        ## If not, the user will not be able to input data
        Goodata = 1

        ##Places the fields into temp variables to put into a class
        firstName = self.firstNameEntry.get()
        lastName = self.lastNameEntry.get()
        suffix = self.suffixEntry.get()
        ASU_ID = self.AngeloIDEntry.get()
        RFID = self.tagEntry.get()
        email = self.emailEntry.get()
        phone = self.phoneEntry.get()
        housing = self.HousingStatusEntry.get()

        ##checks input for any errors
        ##Might need create a function to check for bad data

        ##First and last Name checks
        if (len(firstName) > 26 or len(firstName) < 2 or len(lastName) > 26 or len(lastName) < 2):
            messagebox.showerror(title = "Check Names Length", message = "Either  first name or last Name was either too short or long.")
            Goodata += 1
        if (self.stringCheckForNumers(firstName) or self.stringCheckForNumers(lastName)):
            messagebox.showerror(title = "Number Fail",  message = "No numbers are allowed in either the first or last name fields.")
            Goodata += 1
        
        ##checks Suffix for numbers
        if (self.stringCheckForLetters(suffix)):
            messagebox.showerror(title = "Suffix Fail", message = "No numbers are allowed in the suffix field.")
            Goodata += 1
        
        
        ## if there were no errors, the infomation gets inputed
        if (Goodata == 1):
             temp_person = people(firstName,lastName,suffix,ASU_ID,RFID,email,phone,housing)
             ##DEBUG PRINT STATMENTS
             ## print(firstName)
             ## print(lastName)
             ## print(suffix)
             ## print(ASU_ID)
             ##Inputs the entry into the database
             inputDataBase.inputBasicInfoPeople(temp_person)
             ## print("INPUTED GUI DEBUG") // DEBUG PRINT STAMTENT
             ##Prints in console if the entry did get inputted correctly
             readFromDataBase.readPeopleTable()

        ## After the submition to the people table
        ## The boxes should clear the info from the entry wiget
        self.firstNameEntry.delete(0,"end")
        self.lastNameEntry.delete(0,"end")
        self.suffixEntry.delete(0,"end")
        self.AngeloIDEntry.delete(0,"end")
        self.tagEntry.delete(0,"end")
        self.emailEntry.delete(0,"end")
        self.phoneEntry.delete(0,"end")
        self.HousingStatusEntry.delete(0,"end")


        ##Calls deleteAdminFunction now 12-1-2021
        ## self.firstNameEntry.destroy()
        ## self.lastNameEntry.destroy()
        ## self.suffixEntry.destroy()
        ## self.AngeloIDEntry.destroy()
        ## self.tagEntry.destroy()
        ## self.emailEntry.destroy()
        ## self.phoneEntry.destroy()
        ## self.HousingStatusEntry.destroy()
        ## self.insert_Record_Button.destroy()
        self.destroyAllPossibleAdminFields_Buttons()

        self.show_admin_buttons()
        
    def deleteStudentEntrySection(self,event):
        self.destroyAllPossibleAdminFields_Buttons()
        dataBasePeople = []
        dataBasePeople = readFromDataBase.readPeopleTable()
        peopleOptions = []
        
        peopleOptionsCt = 0
        for i in dataBasePeople:
            peopleOptions.append(i[1])

        deleteVar = tk.StringVar()
        self.studentToDelete = ttk.Combobox(self.window, width = 50, textvariable=deleteVar, values=peopleOptions)
        self.studentToDelete.grid(row=8, column=0, sticky=tk.W, pady=5)
        self.createHomeButton()
        #after this creation this is where it needs to delete from database
        #You can do this with a bind or just a button and get the value

    def editToDataBase(self, event):
        temp_info = returnFromDataBase.returnsInfomationFromPeopleTableFromFirstName(savedUserData)
        RFIDLocal = temp_info[5]

        Goodata = 1

        firstName = self.firstNameEntry.get()
        lastName = self.lastNameEntry.get()
        suffix = self.suffixEntry.get()
        ASU_ID = self.AngeloIDEntry.get()
        RFID = self.tagEntry.get()
        email = self.emailEntry.get()
        phone = self.phoneEntry.get()
        housing = self.HousingStatusEntry.get()

       
        updateLocalRFID=RFID

        ##First and last Name checks
        if (len(firstName) > 26 or len(firstName) < 2 or len(lastName) > 26 or len(lastName) < 2):
            messagebox.showerror(title = "Check Names Length", message = "Either  first name or last Name was either too short or long.")
            Goodata += 1
        if (self.stringCheckForNumers(firstName) or self.stringCheckForNumers(lastName)):
            messagebox.showerror(title = "Number Fail",  message = "No numbers are allowed in either the first or last name fields.")
            Goodata += 1
        
        ##checks Suffix for numbers
        if (self.stringCheckForNumers(suffix)):
             messagebox.showerror(title = "Suffix Fail", message = "No numbers are allowed in the suffix field.")
             Goodata += 1

        if (Goodata == 1):
            temp_person = people(firstName,lastName,suffix,ASU_ID,RFID,email,phone,housing)

            tempID = returnFromDataBase.returnsKeyIDPeopleTableFromRFIDTag(RFIDLocal)
            tempID = tempID[0]
            updateToDataBase.updatePersonFromKeyId(tempID,temp_person)   

    def editStudentsEntrySection(self,event):
        self.destroyAllPossibleAdminFields_Buttons()
        dataBasePeople = []
        dataBasePeople = readFromDataBase.readPeopleTable()
        peopleOptions = []
        

        peopleOptionsCt = 0
        for i in dataBasePeople:
            peopleOptions.append(i[1])

        studentVar = tk.StringVar()
        self.studentChosen = ttk.Combobox(self.window, width = 50, textvariable=studentVar, values=peopleOptions)
        self.studentChosen.grid(row=8, column=0, sticky=tk.W, pady=5)
        self.studentChosen.bind("<Return>", self.showPossibleStudentEdits)
        self.createHomeButton()
    
    def showPossibleStudentEdits(self, event):
        
        ##When the button is pressed, delete these buttons that are in the way
        ##selectedStudent is the
        selectedStudent = self.studentChosen.get()
        global savedUserData
        savedUserData = selectedStudent
        self.destroyAllPossibleAdminFields_Buttons()
        studentData = returnFromDataBase.returnsInfomationFromPeopleTableFromFirstName(selectedStudent)
        print("Start \n\n", studentData, "End \n\n")
        self.firstNameEntry = ttk.Entry(self.window, width=50)
        self.firstNameEntry.grid(row=8, column=0, sticky=tk.W, pady=5)
        self.firstNameEntry.insert(tk.END, studentData[1])
        self.firstNameEntry.bind("<Return>", self.editToDataBase)

        self.lastNameEntry = ttk.Entry(self.window, width=50)
        self.lastNameEntry.grid(row=9, column=0, sticky=tk.W, pady=5)
        self.lastNameEntry.insert(tk.END, studentData[2])
        self.lastNameEntry.bind("<Return>", self.editToDataBase)

        self.suffixEntry = ttk.Entry(self.window, width=50)
        self.suffixEntry.grid(row=10, column=0, sticky=tk.W, pady=5)
        self.suffixEntry.insert(tk.END, studentData[3])
        self.suffixEntry.bind("<Return>", self.editToDataBase)

        self.AngeloIDEntry = ttk.Entry(self.window, width=50)
        self.AngeloIDEntry.grid(row=11, column=0, sticky=tk.W, pady=5)
        self.AngeloIDEntry.insert(tk.END, studentData[4])
        self.AngeloIDEntry.bind("<Return>", self.editToDataBase)

        self.tagEntry = ttk.Entry(self.window, width=50)
        self.tagEntry.grid(row=12, column=0, sticky=tk.W, pady=5)
        self.tagEntry.insert(tk.END, studentData[5])
        self.tagEntry.bind("<Return>", self.editToDataBase)


        self.emailEntry = ttk.Entry(self.window, width=50)
        self.emailEntry.grid(row=13, column=0, sticky=tk.W, pady=5)
        self.emailEntry.insert(tk.END, studentData[6])
        self.emailEntry.bind("<Return>", self.editToDataBase)

        self.phoneEntry = ttk.Entry(self.window, width=50)
        self.phoneEntry.grid(row=14, column=0, sticky=tk.W, pady=5)
        self.phoneEntry.insert(tk.END, studentData[7])
        self.phoneEntry.bind("<Return>", self.editToDataBase)

        self.HousingStatusEntry = ttk.Entry(self.window, width=50)
        self.HousingStatusEntry.grid(row=15, column=0, sticky=tk.W, pady=5)
        self.HousingStatusEntry.insert(tk.END,  studentData[8])
        self.HousingStatusEntry.bind("<Return>", self.editToDataBase)

        self.insert_Record_Button = tk.Button(self.window, text="Update Users")
        self.insert_Record_Button.grid(row=17, column=0, sticky=tk.W, pady=5)
        self.insert_Record_Button.bind("<Button>", self.editToDataBase)

        var = tk.IntVar()
        var.set(1)
        self.isPofessorButton = tk.Radiobutton(self.window, text='is Professor?', variable=var, value=1,)
        self.isPofessorButton.grid(row=16, column=0, sticky=tk.W, pady=5)
        #self.isPofessorButton.bind("<Button>", self.addToDatabase)

        self.isPofessorButton2 = tk.Radiobutton(self.window, text='is not Professor?', variable=var, value=2)
        self.isPofessorButton2.grid(row=16, column=1, sticky=tk.W, pady=5)

        print(var)

        self.homeButton = tk.Button(self.window, text="Home",width=12,height=5)
        self.homeButton.grid(row=18,column=0,rowspan=2,sticky=tk.W)
        self.homeButton.bind("<Button>", self.goHome)
    
    def createClassroomEntrySection(self,event):
        self.destroyAllPossibleAdminFields_Buttons()
       
        self.insertCourseName = tk.Entry(self.window, width=50)
        self.insertCourseName.grid(row=8, column=0, sticky=tk.W, pady=5)
        self.insertCourseName.insert(tk.END, "insert Course Name")
        self.insertCourseName.bind("<Return>", self.addToDatabase)

        self.insertBuildingName = tk.Entry(self.window, width=50)
        self.insertBuildingName.grid(row=9, column=0, sticky=tk.W, pady=5)
        self.insertBuildingName.insert(tk.END, "insert Building Name")
        self.insertBuildingName.bind("<Return>", self.addToDatabase)

        self.insertRoomName = tk.Entry(self.window, width=50)
        self.insertRoomName.grid(row=10, column=0, sticky=tk.W, pady=5)
        self.insertRoomName.insert(tk.END, "insert RoomName")
        self.insertRoomName.bind("<Return>", self.addToDatabase)

        self.insertRoomClassSize = tk.Entry(self.window, width=50)
        self.insertRoomClassSize.grid(row=11, column=0, sticky=tk.W, pady=5)
        self.insertRoomClassSize.insert(tk.END, "insert Room Class Size")
        self.insertRoomClassSize.bind("<Return>", self.addToDatabase)

        self.insertStartDate = tk.Entry(self.window, width=50)
        self.insertStartDate.grid(row=12, column=0, sticky=tk.W, pady=5)
        self.insertStartDate.insert(tk.END, "insert Start Date")
        self.insertStartDate.bind("<Return>", self.addToDatabase)

        self.insertEndDate = tk.Entry(self.window, width=50)
        self.insertEndDate.grid(row=13, column=0, sticky=tk.W, pady=5)
        self.insertEndDate.insert(tk.END, "insert End Date")
        self.insertEndDate.bind("<Return>", self.addToDatabase)

        self.insertTime = tk.Entry(self.window, width=50)
        self.insertTime.grid(row=14, column=0, sticky=tk.W, pady=5)
        self.insertTime.insert(tk.END, "insert Time")
        self.insertTime.bind("<Return>", self.addToDatabase)
        
        

        self.homeButton = tk.Button(self.window, text="Home",width=12,height=5)
        self.homeButton.grid(row=15,column=0,sticky=tk.W)
        self.homeButton.bind("<Button>", self.goHome)

    ## function that create the entry fields for showAdminPowers()
    def createStudentsEntrySection(self,event):

        ##When the button is pressed, delete these buttons that are in the way
        ## Possible change soon
        ##Changed 12-1-2021
        ## self.entryButtonSection.destroy()
        ## self.createClassRoom.destroy()
        ## self.tempButton2.destroy()
        ## self.tempButton3.destroy()
        ## self.tempButton4.destroy()
        ## self.tempButton5.destroy()
        self.destroyAllPossibleAdminFields_Buttons()
       



        ##Moved to the create_class function
        ## self.classroom = ttk.Entry(self.window, width=50)
        ## self.classroom.grid(row=7, column=0, sticky=tk.W, pady=5)
        ## self.classroom.insert(tk.END, "Enter the class size you want (Perfect Square)")
        ## self.classroom.bind("<Return>", self.create_class)

        self.firstNameEntry = ttk.Entry(self.window, width=50)
        self.firstNameEntry.grid(row=8, column=0,columnspan=2, sticky=tk.W, pady=5)
        self.firstNameEntry.insert(tk.END, """Enter a "new Students" First Name""")
        self.firstNameEntry.bind("<Return>", self.addToDatabase)

        self.lastNameEntry = ttk.Entry(self.window, width=50)
        self.lastNameEntry.grid(row=9, column=0,columnspan=2, sticky=tk.W, pady=5)
        self.lastNameEntry.insert(tk.END, """Enter a "new Students" Last Name""")
        self.lastNameEntry.bind("<Return>", self.addToDatabase)

        self.suffixEntry = ttk.Entry(self.window, width=50)
        self.suffixEntry.grid(row=10, column=0,columnspan=2, sticky=tk.W, pady=5)
        self.suffixEntry.insert(tk.END, """Enter a "new Students" Suffix""")
        self.suffixEntry.bind("<Return>", self.addToDatabase)

        self.AngeloIDEntry = ttk.Entry(self.window, width=50)
        self.AngeloIDEntry.grid(row=11, column=0,columnspan=2, sticky=tk.W, pady=5)
        self.AngeloIDEntry.insert(tk.END, """Enter a "new Students" Angelo ID """)
        self.AngeloIDEntry.bind("<Return>", self.addToDatabase)

        self.tagEntry = ttk.Entry(self.window, width=50)
        self.tagEntry.grid(row=12, column=0,columnspan=2, sticky=tk.W, pady=5)
        self.tagEntry.insert(tk.END, """Enter a "new Students" RFID tag""")
        self.tagEntry.bind("<Return>", self.addToDatabase)

        self.phoneEntry = ttk.Entry(self.window, width=50)
        self.phoneEntry.grid(row=13, column=0,columnspan=2, sticky=tk.W, pady=5)
        self.phoneEntry.insert(tk.END, """Enter a "new Students" phoneNumber""")
        self.phoneEntry.bind("<Return>", self.addToDatabase)

        self.emailEntry = ttk.Entry(self.window, width=50)
        self.emailEntry.grid(row=14, column=0,columnspan=2, sticky=tk.W, pady=5)
        self.emailEntry.insert(tk.END, """Enter a "new Students" email""")
        self.emailEntry.bind("<Return>", self.addToDatabase)
    
        self.HousingStatusEntry = ttk.Entry(self.window, width=50)
        self.HousingStatusEntry.grid(row=15, column=0,columnspan=2, sticky=tk.W, pady=5)
        self.HousingStatusEntry.insert(tk.END, """Enter a "new Students" Housing Situation""")
        self.HousingStatusEntry.bind("<Return>", self.addToDatabase)    
        
        ##Update button, I just wanted a GUI way approach to adding People to the Database
        ## WIP: SHIT DOESN"TT WORK DOES NOT WORK - IGGY
        #fixed button, moved button to admin powers. figured it would make it appear and disappear correctly
        self.insert_Record_Button = tk.Button(self.window, text="Insert Users")
        self.insert_Record_Button.grid(row=16, column=0, sticky=tk.W, pady=5)
        self.insert_Record_Button.bind("<Button>", self.addToDatabase)

        var = tk.IntVar()
        self.isPofessorButton = tk.Radiobutton(self.window, text='is Professor?', variable=var, value=1)
        self.isPofessorButton.grid(row=16, column=1, sticky=tk.W, pady=5)
        self.isPofessorButton.bind("")
        #self.isPofessorButton.bind("<Button>", self.addToDatabase)
        self.isPofessorButton2 = tk.Radiobutton(self.window, text='is not Professor?', variable=var, value=2)
        self.isPofessorButton2.grid(row=16, column=2, sticky=tk.W, pady=5)

        self.createHomeButton()       

    def destroyAllPossibleAdminFields_Buttons(self):
        try:
            self.entryButtonSection.destroy()
        except:
            pass
        try:
            self.createClassRoom.destroy()
        except:
            pass
        try:
            self.showClass.destroy()
        except:
            pass
        try:
            self.editPersonButton.destroy()
        except:
            pass
        try:
            self.editClassroomButton.destroy()
        except:
            pass
        try:
            self.deletePersonButton.destroy()
        except:
            pass
        try:
            self.classroom.destroy()
        except:
            pass
        try:
            self.firstNameEntry.destroy()
        except:
            pass
        try:
            self.lastNameEntry.destroy()
        except:
            pass
        try:
            self.suffixEntry.destroy()
        except:
            pass
        try:
            self.AngeloIDEntry.destroy()
        except:
            pass
        try:
            self.tagEntry.destroy()
        except:
            pass
        try:
            self.emailEntry.destroy()
        except:
            pass
        try:
            self.phoneEntry.destroy()
        except:
            pass
        try:
            self.HousingStatusEntry.destroy()
        except:
            pass
        try:
            self.insert_Record_Button.destroy()
        except:
            pass
        try:
            self.homeButton.destroy()
        except:
            pass
        try:
            self.signOutbutton.destroy()
        except:
            pass
        try:
            self.isPofessorButton.destroy()
        except:
            pass
        try:
            self.studentChosen.destroy()
        except:
            pass
        try:
            self.studentToDelete.destroy()
        except:
            pass
        try:
            self.insertCourseName.destroy()
        except:
            pass
        try:
            self.insertBuildingName.destroy()
        except:
            pass
        try:
            self.insertRoomName.destroy()
        except:
            pass
        try:
            self.insertRoomClassSize.destroy()
        except:
            pass
        try:
            self.insertStartDate.destroy()
        except:
            pass
        try:
            self.insertEndDate.destroy()
        except:
            pass
        try:
            self.insertTime.destroy()
        except:
            pass
        try:
            self.isPofessorButton2.destroy()
        except:
            pass

    ##Creating the button for the signout after the good login
    def SignOutButton(self):
        self.signOutbutton = tk.Button(self.window, text="Sign Out",width=12,height=5)
        self.signOutbutton.grid(row=18, column=0, rowspan=2,columnspan=2,
         sticky=tk.W,)

        self.signOutbutton.bind("<Button>", self.signOutFunction)
    
    ##creates the function after pressing said signoutButton
    def signOutFunction(self,event):
        self.destroyAllPossibleAdminFields_Buttons()
        exit()
        self.signOutbutton.destroy()
        self.loginTime.destroy()
        self.recentUser.destroy()
        self.create_widgets()

    ##A function to create the Home Button
    def createHomeButton(self):
        self.homeButton = tk.Button(self.window, text="Home",width=12,height=5)
        self.homeButton.grid(row=18,column=0,rowspan=2,columnspan=2,sticky=tk.W)
        self.homeButton.bind("<Button>", self.goHome)

    ##A function to bind the home button to to make it go to the home
    def goHome(self,event):
        self.destroyAllPossibleAdminFields_Buttons()
        self.show_admin_powers()
    
    #(Comments written 10/21/21. This is only the outline of what the UI needs to do)
    #The UI needs to display the classroom and the positions of the users
    def create_widgets(self):
    #creating the user interface
        self.title = ttk.Label(self.window, text="RFID COVID-19 Tracker")
        self.title.config(anchor=CENTER)
        self.title.grid(row=0, column=0,columnspan=5)

        print("createdWiget")
        #setting up when the user can enter a username
        self.name_entry = ttk.Entry(self.window, width=25)
        self.name_entry.grid(row=1, column=0, sticky=tk.W, pady=5,columnspan=5)
        self.name_entry.insert(tk.END, "Iggy")
        self.name_entry.bind("<Return>", self.validLogin)
        
        #setting up when the user can enter a password
        self.password_entry = ttk.Entry(self.window, width=25)
        self.password_entry.grid(row=2, column=0, sticky=tk.W, pady=5,columnspan=5)
        self.password_entry.insert(tk.END, "Hello")
        self.password_entry.bind("<Return>", self.validLogin)
        
        #creating a button to login to the application
        self.login_button = tk.Button(self.window, text="Log in")
        self.login_button.grid(row=3, column=0, sticky=tk.W, pady=5)
        self.login_button.bind("<Button>", self.validLogin)
            
        #creating a label for most recent log in
        ##Commenting this for now.
        ##could reuse this for feature later
        ## self.recentTag = ttk.Label(self.window, text="This is the most Recent login")
        ## self.recentTag.grid(row=5, column=0,sticky=tk.W, pady=20)

        #creating the the display to show if a user is logged in
        self.recentUser = ttk.Label(self.window)
        self.recentUser.grid(row=6, column=0,sticky=tk.W, pady=20)
        #always create a home button (does not need to be placed) so it can be deleted

        
        
        #The Following code is for the display of seats. The seats are represented by brackets and can be empty
    
    ##Small fucntion to check for numbers in a string
    def stringCheckForNumers(self,string):
        return any(character.isdigit() for character in string)
    
    ##Small function to checkl for letters in a string ##Built for the error checking in phone number field.+--.
    def stringCheckForLetters(self,string):
        return any(character.isalpha() for character in string)
        
if __name__ == "__main__":
    main()