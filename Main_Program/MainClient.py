
import dataBaseCode
from Class import people
from dataBaseCode import createTables
from dataBaseCode import inputBasicInfoPeople
from dataBaseCode import readPeopleTable
from dataBaseCode import deleteBasicInfoPeople
from dataBaseCode import readProfTable
from dataBaseCode import returnsKeyIDPeopleTableFromRFIDTag
from dataBaseCode import inputProfessor
from dataBaseCode import deleteProfessor
#from dataBaseCode import createProfessorTable
from GUICode import RFIDDisplay
#isAdminFromPersonID


def testCode():

    createTables()
    #createProfessorTable()
    #print("hello")
    #testInputName1 = people("Iggy", "Flowers", "None",999_999, "AB:CD:EF:GH","potato@gmail.com", 111_101_1111, "On_Campus")
    #inputBasicInfoPeople(testInputName1)
    #testInputName2 = people("JP", "Powers", "None",999_998, "AA:AA:CC:AA","JP@gmail.com", 121_101_2222, "OFF_Campus")
    #inputBasicInfoPeople(testInputName2)
    #testInputName3 = people("Dogdu", "Erodgon", "Ph.D",999_997, "AA:AA:EE:EE","ERROR@gmail.com", 111_101_3333, "OFF_Campus")
    #inputBasicInfoPeople(testInputName3)
    #x = input("Test")
    #print(x)
    #x = returnsKeyIDPeopleTableFromRFIDTag("AB:CD:EF:GH")
    #print (x)

    #deleteProfessor(1)
    #inputProfessor()
    readPeopleTable()
    #print("-----------------")
    readProfTable()
    #deleteBasicInfoPeople(2)
    #readTable("people")

    RFIDDisplay.isAdminFromPersonID(1)

    #creating program
    #program = RFIDDisplay()
    #starting event loop
    #pogram.window.mainloop()

def main():
    ## testCode is just the temp function to test datavbase or GUI code
    testCode()

if __name__ == "__main__":
    main()