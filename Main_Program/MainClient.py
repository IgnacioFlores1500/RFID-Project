
import dataBaseCode
from Class import people
from dataBaseCode import createTables
from dataBaseCode import inputBasicInfoPeople
from dataBaseCode import readPeopleTable
from dataBaseCode import deleteBasicInfoPeople

def main():
    createTables()
    print("hello")
    #testInputName = people("Iggy", "Flowers", "None",999_999, "AB:CD:EF:GH","potato@gmail.com", 111_101_1111, "On_Campus")
    #inputBasicInfoPeople(testInputName)

    #readTable("people")
    #deleteBasicInfoPeople(2)
    #readTable("people")


if __name__ == "__main__":
    main()
