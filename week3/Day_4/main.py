from college import Faculty, Department, Subject, Course, Exam, Student, Professor

_Faculty = []
_Departments = []
_Subjects = []
_Courses = []
_Exams = []
_Students = []
_Professors = []





def faculty_menu():
    print("\npress 1 to create Faculty: ")
    print("press 2 to read from Faculty: ")
    print("press 3 to update Faculty: ")
    print("press 4 to show menu: ")
    print("press 5 to get the professors who work in the Faculty: ")
    print("press 6 to get the departments that are existed in the Faculty: ")
    print("press 7 to exit: ")

faculty = Faculty.Faculty()
professor = Professor.Professor()
department = Department.Department()

faculty_menu()
while True:
    choice = int(input("\nPlease enter your choice: "))

    if choice == 1:
        proNum = int(input("\nPlease enter professors and departments numbers in the Faculty: "))
        dNum = int(input())
        faculty.createFaculty(proNum, dNum)

    elif choice == 2:
        print(faculty.readFaculty())

    elif choice == 3:
        faculty.updateFaculty()

    elif choice == 4:
        faculty_menu()

    elif choice == 5:
        faculty.readFaculty_Professor(professor.readProfessor())

    elif choice == 6:
        faculty.readFaculty_Department(department.readDepartment())

    elif choice == 7:
        break

    else:
        print("Sorry invalid input")




def department_menu():
    print("\npress 1 to create Department: ")
    print("press 2 to read from Department: ")
    print("press 3 to read from a specific Department: ")
    print("press 4 to update a specific Department: ")
    print("press 5 to show menu: ")
    print("press 6 to exit: ")




department_menu()
while True:
    choice = int(input("\nPlease enter your choice: "))

    if choice == 1:
        depNum = int(input("Please enter department numbers: "))
        department.createDepartment(depNum)

    elif choice == 2:
        print(department.readDepartment())

    elif choice == 3:
        print(department.readSpecificDep(depNum))

    elif choice == 4:
        department.updateSpecificDepInfo(depNum)

    elif choice == 5:
        department_menu()
    
    elif choice == 6:
        break

    else:
        print("Sorry invalid input")

    

def subjects_menu():
    print("\npress 1 to create Subject: ")
    print("press 2 to read from Subject: ")
    print("press 3 to read from a specific Subject: ")
    print("press 4 to update a specific Subject: ")
    print("press 5 to show menu: ")
    print("press 6 to exit: ")

subject = Subject.Subject()

subjects_menu()
while True:
    choice = int(input("\nPlease enter your choice: "))

    if choice == 1:
        subNum = int(input("Please enter subjects numbers: "))
        subject.createSubject(subNum)

    elif choice == 2:
        print(subject.readSubject())

    elif choice == 3:
        print(subject.readSpecificSubjectInfo(subNum))

    elif choice == 4:
        subject.updateSpecificSubInfo(subNum)

    elif choice == 5:
        subjects_menu()

    elif choice == 6:
        break

    else:
        print("Sorry invalid input")





def courses_menu():
    print("\npress 1 to create Course: ")
    print("press 2 to read from Course: ")
    print("press 3 to read from a specific Course: ")
    print("press 4 to update a specific Course: ")
    print("press 5 to show menu: ")
    print("press 6 to exit: ")

course = Course.Course()

courses_menu()
while True:
    choice = int(input("\nPlease enter your choice: "))

    if choice == 1:
        courseNum = int(input("Please enter Courses numbers: "))
        course.createCourse(courseNum)

    elif choice == 2:
        print(course.readCourse())

    elif choice == 3:
        print(course.readSpecificCourseInfo(courseNum))

    elif choice == 4:
        course.updateSpecificCourseInfo(courseNum)

    elif choice == 5:
        courses_menu()

    elif choice == 6:
        break

    else:
        print("Sorry invalid input")






def exams_menu():
    print("\npress 1 to create Exam: ")
    print("press 2 to read from Exam: ")
    print("press 3 to read from a specific Exam: ")
    print("press 4 to update a specific Exam: ")
    print("press 5 to show menu: ")
    print("press 6 to exit: ")

exam = Exam.Exam()

exams_menu()
while True:
    choice = int(input("\nPlease enter your choice: "))

    if choice == 1:
        examNum = int(input("Please enter Exams numbers: "))
        exam.createExam(examNum)

    elif choice == 2:
        print(exam.readExam())

    elif choice == 3:
        print(exam.readSpecificExamInfo(examNum))

    elif choice == 4:
        exam.updateSpecificExamInfo(examNum)

    elif choice == 5:
        exams_menu()

    else:
        break






def students_menu():
    print("\npress 1 to create Student: ")
    print("press 2 to read from Student: ")
    print("press 3 to read from a specific Student: ")
    print("press 4 to update a specific Student: ")
    print("press 5 to show menu: ")
    print("press 6 to exit: ")

student = Student.Student()

students_menu()
while True:
    choice = int(input("\nPlease enter your choice: "))

    if choice == 1:
        studNum = int(input("Please enter Students numbers: "))
        student.createStudent(studNum)

    elif choice == 2:
        print(student.readStudent())

    elif choice == 3:
        print(student.readSpecificStudentInfo(studNum))

    elif choice == 4:
        student.updateSpecificStudentInfo(studNum)

    elif choice == 5:
        students_menu()

    else:
        break





def professors_menu():
    print("\npress 1 to create Professors: ")
    print("press 2 to read from Professors: ")
    print("press 3 to read from a specific Professor: ")
    print("press 4 to update a specific Professor: ")
    print("press 5 to show menu: ")
    print("press 6 to get what subjects are taught by which professor: ")
    print("press 7 to get what courses are taught by which professor: ")
    print("press 8 to exit: ")



professors_menu()
while True:
    choice = int(input("\nPlease enter your choice: "))

    if choice == 1:
        profNum = int(input("Please enter Professors numbers: "))
        professor.createProfessor(profNum)

    elif choice == 2:
        print(professor.readProfessor())

    elif choice == 3:
        print(professor.readSpecificProfessorInfo(profNum))

    elif choice == 4:
        professor.updateSpecificProfessorInfo(profNum)

    elif choice == 5:
        professors_menu()

    elif choice == 6:
        professor.readProfessor_Subject(subject.readSubject())

    elif choice == 7:
        professor.readProfessor_Course(course.readCourse())
    else:
        break




# #====================================================================

print("\nFaculty Info: " + str(faculty.readFaculty()))
print("\nDepartments Info: " + str(department.readDepartment()))
print("\nSubjects Info: " + str(subject.readSubject()))
print("\nCourses Info: " + str(course.readCourse()))
print("\nExams Info: " + str(exam.readExam()))
print("\nStudents Info: " + str(student.readStudent()))
print("\nProfessors Info: " + str(professor.readProfessor()))



print("\nMade With Love By (XWARE BOOT CAMP)")


# #==========================================================









            


