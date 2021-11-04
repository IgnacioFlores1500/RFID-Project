#This program is designed to display information from a sql data base and set a "classroom" with students
#The program is specifically designed for the RFID scanner used in software engineering fall 2021
#JohnPaul Flores is the sole author of this code as of 10/21/21
#Software Engineering
#JohnPaul Flores CID: 81340848
#Last Edited: Date 10/21/21


# To use the "generic" widgets
import tkinter as tk
# To use the stylized, "look-and-feel" widgets
from tkinter import ttk
# To display any error or warnings for mistakes, and to make sure the user wants to enter the info
from tkinter import messagebox
# sublibrary to ask for any info the program needs from the user 
from tkinter import simpledialog
# add secondary file using info validator

def main():
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
    def isAdmin(self, event, accounts):
        #taking data entered into the entry and chcecking it for authentification
        enteredName = self.my_entry.get()
        
        #if whatever information is true then 
        for users in accounts:
            if users == enteredName:
                return True
        return False

    #validPassword takes what the user entered into the passwd box and sees if the password 
    #and username match the ones in the data base
    def validPassword (EnteredPasswd, accounts):
        #a variable that is present to check if the username is registered in the data base
        isPasswdRegistered = False
        
        #check the passwords for each account and see if they match
        for passwd in accounts.keys:
            if passwd == enteredPasswd:
                return True
        
    #(Comments written 10/21/21. This is only the outline of what the UI needs to do)
    #The UI needs to display the classroom and the positions of the users
    def create_widgets(self):
    #creating the user interface
        self.title = ttk.Label(self.window, text="RFID COVID-19 Tracker")
        self.title.grid(row=0, column=0)

        #setting up when the user can enter a username
        self.name_entry = ttk.Entry(self.window, width=100)
        self.name_entry.grid(row=1, column=0, sticky=tk.W, pady=10)
        self.name_entry.insert(tk.END, "Enter User Name")
        self.name_entry.bind("<Return>", self.isAdmin)
        
        #setting up when the user can enter a password
        self.password_entry = ttk.Entry(self.window, width=100)
        self.password_entry.grid(row=2, column=0, sticky=tk.W, pady=10)
        self.password_entry.insert(tk.END, "Enter Password")
        self.password_entry.bind("<Return>", self.validPassword)
    
        #The Following code is for the display of seats. The seats are represented by brackets and can be empty
        
if __name__ == "__main__":
    main()
