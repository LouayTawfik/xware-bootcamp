class Exam:
    def __init__(self) -> None:
        self.exams = []

    def createExam(self, examNum):
        for i in range(examNum):
            exam = {}
            exam['id'] = input("Please enter exam id number " + str(i + 1) + ": ")
            exam['name'] = input("Please enter exam name number " + str(i + 1) + ": ")
            exam['code'] = input("Please enter exam code number " + str(i + 1) + ": ")
            exam['time'] = input("Please enter exam time number " + str(i + 1) + ": ")
            exam['date'] = input("Please enter exam date number " + str(i + 1) + ": ")

            self.exams.append(exam)





    def readExam(self):
        return self.exams



    def readSpecificExamInfo(self, examNum):
        examInfoNum = int(input("Please choose the Exam you want to read: "))
        examInfoNum -= 1

        for i in range(examNum):
            if i == examInfoNum:
                key = input("Please choose the name of Exam info you want to read: ")
                return self.exams[examInfoNum][key]


    def updateSpecificExamInfo(self, examNum):
        choosenExamNum = int(input("Please choose the Exam you want to update: "))
        choosenExamNum -= 1

        for i in range(examNum):
            if i == choosenExamNum:
                key = input("Please choose the name of Exam info you want to update: ")
                self.exams[i][key] = input("Please enter new " + key + " for the choosen Exam: ")
                print(f"The Exam ", key, " is updated successfully")