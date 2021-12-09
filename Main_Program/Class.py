



class people:
    #Note to self, we need to write a key function to write new keys
    #FIXED: Look at Commit 10/22/2021
    def __init__(self, firstName,lastName, Suffix, ASUID, RFID, Email, Phone, CampusOFFCampus):
        #self.key = key
        self.firstName = firstName
        self.lastName = lastName
        self.Suffix = Suffix
        self.ASUID = ASUID
        self.RFID = RFID
        self.Email = Email
        self.Phone = Phone
        self.CampusOFFCampus = CampusOFFCampus

class courses:
    def __init__(self, courseName, buildingName, roomNumber, roomClassSize, startDate, endDate, time):
        self.courseName = courseName
        self.buildingName = buildingName
        self.roomNumber = roomNumber
        self.roomClassSize = roomClassSize
        self.startDate = startDate
        self.endDate = endDate
        self.time = time


    

        
    

       
    




#Iggy = student(1, 'Ignacio', 'Flores', 100000, 'Campus')

#print(Iggy.getKey())


