
import dataBaseCode
from Class import people
from dataBaseCode import createTables
from dataBaseCode import inputBasicInfoPeople
from dataBaseCode import readPeopleTable
from dataBaseCode import deleteBasicInfoPeople
from dataBaseCode import readProfTable
#from dataBaseCode import createProfessorTable
from GUICode import RFIDDisplay

def main():
    createTables()
    #createProfessorTable()
    print("hello")
    #testInputName = people("Iggy", "Flowers", "None",999_999, "AB:CD:EF:GH","potato@gmail.com", 111_101_1111, "On_Campus")
    #inputBasicInfoPeople(testInputName)
    
    #readPeopleTable()
    readProfTable()
    #deleteBasicInfoPeople(2)
    #readTable("people")


    #creating program
    #program = RFIDDisplay()
    #starting event loop
    #program.window.mainloop()


if __name__ == "__main__":
    main()
