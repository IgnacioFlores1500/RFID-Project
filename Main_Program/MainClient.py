
import dataBaseCode
from Class import people
from dataBaseCode import createTables
# #from dataBaseCode import inputBasicInfoPeople
# from dataBaseCode import readPeopleTable
# from dataBaseCode import deleteBasicInfoPeople
# from dataBaseCode import readProfTable
# from dataBaseCode import returnsKeyIDPeopleTableFromRFIDTag
# #from dataBaseCode import inputProfessor
# from dataBaseCode import deleteProfessor
# from dataBaseCode import returnsInfomationFromPeopleTableFromFirstName

## These are classes that are related to it's name. EX: inputDataBase involves all functions releated to inputing data into the DB. 
from dataBaseCode import inputDataBase
from dataBaseCode import returnFromDataBase
from dataBaseCode import readFromDataBase
from dataBaseCode import deleteFromDataBase

#from dataBaseCode import createProfessorTable
from GUICode import RFIDDisplay
#isAdminFromPersonID


def testCode():


    ##Creates Tables, sends a error or a string saying that tables have been made already
    createTables()

    ##read from database
    readFromDataBase.readPeopleTable()

    ##Nice hello Statment : )
    print("hello")

    ##List of testObjects to input data
    # testInputName1 = people("Iggy", "Flowers", "None",999_999, "AB:CD:EF:GH","potato@gmail.com", 111_101_1111, "On_Campus")
    # inputDataBase.inputBasicInfoPeople(testInputName1)
    # testInputName2 = people("JP", "Powers", "None",999_998, "AA:AA:CC:AA","JP@gmail.com", 121_101_2222, "OFF_Campus")
    # inputDataBase.inputBasicInfoPeople(testInputName2)
    # testInputName3 = people("Dogdu", "Erodgon", "Ph.D",999_997, "AA:AA:EE:EE","ERROR@gmail.com", 111_101_3333, "OFF_Campus")
    # inputDataBase.inputBasicInfoPeople(testInputName3)
    
    ## Shows example of how to return a certain person from the database from RFID
    ##returns none if there is noneone witht htat RFID
    ##x = returnFromDataBase.returnsKeyIDPeopleTableFromRFIDTag("AB:CD:EF:IK")
    ##print (x)


    ##DeleteFrom the professor Database using ProfID
    ##deleteFromDataBase.deleteProfessor(2)
    #deleteFromDataBase.deleteBasicInfoPeople(6)

    ##Input a person into the professor table with KeyID: NOTE must be in the people table
    ##inputDataBase.inputProfessor()


    ##Read Tables 
    ##readFromDataBase.readPeopleTable()
    
    ##readFromDataBase.readProfTable()


    
 
    ##Ignore this part of the demo
    # firstName = "Bob"
    # x = returnsInfomationFromPeopleTableFromFirstName(firstName)
    
    # if (x):
    #     print ("YIKES")
    # else: 
    #     print("FALSE")
    #RFIDDisplay.isAdminFromPersonID(1)


    ##JP's GUI main Code
    ##creating program
    program = RFIDDisplay()
    ##starting event loop
    program.window.mainloop()

def main():
    ## testCode is just the temp function to test datavbase or GUI code
    testCode()

if __name__ == "__main__":
    main()