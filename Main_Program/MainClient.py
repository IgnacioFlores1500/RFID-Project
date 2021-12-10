

import dataBaseCode
from Class import people
from Class import courses
from dataBaseCode import createTables


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
    x = readFromDataBase.readPeopleTable()
    print(x)
    ##Nice hello Statment : )
    print("hello")

    ##List of testObjects to input data
    #testInputName1 = people("Iggy", "Flowers", "None",999_999, 1231231321,"potato@gmail.com", 111_101_1111, "On_Campus")
    #inputDataBase.inputBasicInfoPeople(testInputName1)
    #testInputName2 = people("JP", "Powers", "None",999_998, 12313219999,"JP@gmail.com", 121_101_2222, "OFF_Campus")
    #inputDataBase.inputBasicInfoPeople(testInputName2)
    #testInputName3 = people("Dodgdu", "Erodgon", "Ph.D",999_997,770_351_046_990,"ERROR@gmail.com", 111_101_3333, "OFF_Campus")
    #inputDataBase.inputBasicInfoPeople(testInputName3)
    
    ## Shows example of how to return a certain per son from the database from RFID
    ##returns none if there is noneone witht htat RFID
    x = returnFromDataBase.returnsKeyIDPeopleTableFromRFIDTag(770351046990)
    print (x)


    #courseExample = courses("SoftWare Engi", "MCS", 115, 25, 12522, 50522, 900)

    #inputDataBase.inputCourse(courseExample)
    ##DeleteFrom the professor Database using ProfID
    ##deleteFromDataBase.deleteProfessor(2)
    #deleteFromDataBase.deleteBasicInfoPeople(2)1

    ##Input a person into the professor table with KeyID: NOTE must be in the people table
    #inputDataBase.inputProfessor()

    #inputDataBase.inputStudent()


    ##seat x and seat y 
    seatX = 1
    seatY = 3
    #inputDataBase.inputActiveCourse(seatX,seatY)

    ##print(returnFromDataBase.checkSeat(1, 3,1))
    

    ##Read Tables 
    ##readFromDataBase.readPeopleTable()
    
    ##readFromDataBase.readProfTable()

    #readFromDataBase.readCourseTable()
    
    #readFromDataBase.readStudentTable()

    readFromDataBase.readActiveCourseTable()
    ##seat(i=1, j=3, courseID 1)
    # print(returnFromDataBase.checkSeat(1, 3,1))
    # print(returnFromDataBase.checkSeatHealth(1, 3,1))
    # print(readFromDataBase.readActiveCourseTable())
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