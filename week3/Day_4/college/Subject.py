class Subject:
    def __init__(self) -> None:
        self.subjects = []

    def createSubject(self, subNum):
        for i in range(subNum):
            sub = {}
            sub['id'] = input("Please enter subject id number " + str(i + 1) + ": ")
            sub['name'] = input("Please enter subject name number " + str(i + 1) + ": ")
            sub['code'] = input("Please enter subject code number " + str(i + 1) + ": ")

            self.subjects.append(sub)


    def readSubject(self):
        return self.subjects


    def readSpecificSubjectInfo(self, subNum):
        subInfoNum = int(input("Please choose the Subject you want to read: "))
        subInfoNum -= 1

        for i in range(subNum):
            if i == subInfoNum:
                key = input("Please choose the name of Subject info you want to read: ")
                return self.subjects[subInfoNum][key]


    def updateSpecificSubInfo(self, subNum):
        choosenSubNum = int(input("Please choose the Subject you want to update: "))
        choosenSubNum -= 1

        for i in range(subNum):
            if i == choosenSubNum:
                key = input("Please choose the name of Subject info you want to update: ")
                self.subjects[i][key] = input("Please enter new " + key + " for the choosen Subject: ")
                print(f"The Subject ", key, " is updated successfully")
