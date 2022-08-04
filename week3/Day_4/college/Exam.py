def createExam(_Exams, examNum):
    for i in range(examNum):
        exam = {}
        exam['id'] = input("Please enter exam id number " + str(i + 1) + ": ")
        exam['name'] = input("Please enter exam name number " + str(i + 1) + ": ")
        exam['code'] = input("Please enter exam code number " + str(i + 1) + ": ")
        exam['time'] = input("Please enter exam time number " + str(i + 1) + ": ")
        exam['date'] = input("Please enter exam date number " + str(i + 1) + ": ")

        _Exams.append(exam)





def readExam(_Exams):
    print(_Exams)



def readSpecificExamInfo(_Exams, examNum):
    examInfoNum = int(input("Please choose the Exam you want to read: "))
    examInfoNum -= 1

    for i in range(examNum):
        if i == examInfoNum:
            key = input("Please choose the name of Exam info you want to read: ")
            print(_Exams[examInfoNum][key])


def updateSpecificExamInfo(_Exams, examNum):
    choosenExamNum = int(input("Please choose the Exam you want to update: "))
    choosenExamNum -= 1

    for i in range(examNum):
        if i == choosenExamNum:
            key = input("Please choose the name of Exam info you want to update: ")
            _Exams[i][key] = input("Please enter new " + key + " for the choosen Exam: ")