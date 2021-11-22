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
from tkinter import ttk
# To display any error or warnings for mistakes, and to make sure the user wants to enter the info
from tkinter import messagebox
# sublibrary to ask for any info the program needs from the user 
from tkinter import simpledialog
from tkinter.constants import END
# sublibrary to 

##Imports a function from database file to return if a personID has edit_prilvages
from dataBaseCode import returnFromDataBase
#from dataBaseCode import returnsInfomationFromPeopleTableFromFirstName

TrueUser = False
TruePassword = False
CurrentFailedAttempt = False
hasBeenCreated = False
recentClassSize = 0
seats = {}
adminFields = {}
CurrentLogin = ""


def main():
    RecentClassSize = 0
    #creating program
    program = RFIDDisplay()
    #starting event loop
    program.window.mainloop()

class RFIDDisplay:

    def __init__(self):
        #Making the application window
        self.window = tk.Tk()
        self.create_widgets()
        
    
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
            self.login_button.destroy()

            #if the login is valid, show who is logged in
            self.recentUser.destroy()
            self.recentUser = ttk.Label(self.window, text =  " " + user)
            self.recentUser.grid(row=6, column=0,sticky=tk.W, pady=20)

        
        self.create_widgets()
            
    #show admin powers is to enable the ability to change a class and or roster
    def show_admin_powers(self):
        if CurrentFailedAttempt == True:
            self.display.delete(0, END)
            
        self.classroom = ttk.Entry(self.window, width=50)
        self.classroom.grid(row=7, column=0, sticky=tk.W, pady=5)
        self.classroom.insert(tk.END, "Enter the class size you want (Perfect Square)")
        self.classroom.bind("<Return>", self.create_class)

        self.firstNameEntry = ttk.Entry(self.window, width=50)
        self.firstNameEntry.grid(row=8, column=0, sticky=tk.W, pady=5)
        self.firstNameEntry.insert(tk.END, """Enter a "new Students" First Name""")
        self.firstNameEntry.bind("<Return>", self.addToDatabase)

        self.lastNameEntry = ttk.Entry(self.window, width=50)
        self.lastNameEntry.grid(row=9, column=0, sticky=tk.W, pady=5)
        self.lastNameEntry.insert(tk.END, """Enter a "new Students" Last Name""")
        self.lastNameEntry.bind("<Return>", self.addToDatabase)

        self.suffixEntry = ttk.Entry(self.window, width=50)
        self.suffixEntry.grid(row=10, column=0, sticky=tk.W, pady=5)
        self.suffixEntry.insert(tk.END, """Enter a "new Students" Suffix""")
        self.suffixEntry.bind("<Return>", self.addToDatabase)

        self.AngeloIDEntry = ttk.Entry(self.window, width=50)
        self.AngeloIDEntry.grid(row=11, column=0, sticky=tk.W, pady=5)
        self.AngeloIDEntry.insert(tk.END, """Enter a "new Students" Angelo ID """)
        self.AngeloIDEntry.bind("<Return>", self.addToDatabase)

        self.tagEntry = ttk.Entry(self.window, width=50)
        self.tagEntry.grid(row=12, column=0, sticky=tk.W, pady=5)
        self.tagEntry.insert(tk.END, """Enter a "new Students" RFID tag""")
        self.tagEntry.bind("<Return>", self.addToDatabase)

        self.emailEntry = ttk.Entry(self.window, width=50)
        self.emailEntry.grid(row=13, column=0, sticky=tk.W, pady=5)
        self.emailEntry.insert(tk.END, """Enter a "new Students" email""")
        self.emailEntry.bind("<Return>", self.addToDatabase)
    
        self.HousingStatusEntry = ttk.Entry(self.window, width=50)
        self.HousingStatusEntry.grid(row=14, column=0, sticky=tk.W, pady=5)
        self.HousingStatusEntry.insert(tk.END, """Enter a "new Students" Housing Situation""")
        self.HousingStatusEntry.bind("<Return>", self.addToDatabase)    
        
        ##Update button, I just wanted a GUI way approach to adding People to the Database
        ## WIP: SHIT DOESN"TT WORK DOES NOT WORK - IGGY
        #fixed button, moved button to admin powers. figured it would make it appear and disappear correctly
        self.insert_Record_Button = tk.Button(self.window, text="Insert Users")
        self.insert_Record_Button.grid(row=15, column=0, sticky=tk.W, pady=5)
        self.insert_Record_Button.bind("<Button>", self.addToDatabase)
        self.create_widgets()

    #Create class is meant to make the classroom on the UI by making empty seats.
    def create_class(self, event):
        global seats
        global recentClassSize
        hasBeenCreated = True
        global classSize

        classSize = self.classroom.get()
        ###I assume to type_cast classSize from string to integer
        classSize = int(classSize)

        if recentClassSize != 0:
            for i in range(recentClassSize):
                for j in range(3, recentClassSize + 3):
                    seats[(i, j + 3)].destroy()
        #for i in range(RecentClassSize):
            #for j in range(2, RecentClassSize + 2):
                #self.b = ttk.Label(self.window, text="")
                #self.b.grid(row=i, column=j, pady=5)
            
        for i in range(classSize):
            for j in range(3, classSize + 3):
                b = ttk.Label(self.window, text="RFID COVID-19 Tracker")
                b.grid(row=i, column=j, pady=5)
                seats[(i, j + 3)] = b
        
        recentClassSize = classSize
        self.create_widgets()

    #this function is connected to the update database button specifically for 
    #the time being
    def addToDatabase(self):
        hello = 0
        self.create_widgets()

    #(Comments written 10/21/21. This is only the outline of what the UI needs to do)
    #The UI needs to display the classroom and the positions of the users
    def create_widgets(self):
    #creating the user interface
        self.title = ttk.Label(self.window, text="RFID COVID-19 Tracker")
        self.title.grid(row=0, column=0)

        #setting up when the user can enter a username
        self.name_entry = ttk.Entry(self.window, width=50)
        self.name_entry.grid(row=1, column=0, sticky=tk.W, pady=5)
        self.name_entry.insert(tk.END, "GoodBye")
        self.name_entry.bind("<Return>", self.validLogin)
        
        #setting up when the user can enter a password
        self.password_entry = ttk.Entry(self.window, width=50)
        self.password_entry.grid(row=2, column=0, sticky=tk.W, pady=5)
        self.password_entry.insert(tk.END, "Hello")
        self.password_entry.bind("<Return>", self.validLogin)
        
        #creating a button to login to the application
        self.login_button = tk.Button(self.window, text="Log in")
        self.login_button.grid(row=3, column=0, sticky=tk.W, pady=5)
        self.login_button.bind("<Button>", self.validLogin)
            
        #creating a label for most recent log in
        self.recentTag = ttk.Label(self.window, text="This is the most Recent login")
        self.recentTag.grid(row=5, column=0,sticky=tk.W, pady=20)

        #creating the the display to show if a user is logged in
        self.recentUser = ttk.Label(self.window)
        self.recentUser.grid(row=6, column=0,sticky=tk.W, pady=20)
        
        
        #The Following code is for the display of seats. The seats are represented by brackets and can be empty
        
if __name__ == "__main__":
    main()