from college import Faculty, Department, Subject, Course, Exam, Student, Professor



_Faculty = []
_Departments = []
_Subjects = []
_Courses = []
_Exams = []
_Students = []
_Professors = []


Faculty.createFaculty(_Faculty)
Faculty.readFaculty(_Faculty)
Faculty.updateFaculty(_Faculty)
Faculty.readFaculty(_Faculty)


depNum = int(input("Please enter department numbers: "))
Department.createDepartment(_Departments, depNum)
Department.readDepartment(_Departments)

Department.readSpecificDep(_Departments, depNum)
Department.updateSpecificDepInfo(_Departments, depNum)
Department.readDepartment(_Departments)


subNum = int(input("Please enter subject numbers: "))
Subject.createSubject(_Subjects, subNum)
Subject.readSubject(_Subjects)

Subject.readSpecificSubjectInfo(_Subjects, subNum)
Subject.updateSpecificSubInfo(_Subjects, subNum)
Subject.readSubject(_Subjects)


courseNum = int(input("Please enter course numbers: "))
Course.createCourse(_Courses, courseNum)
Course.readCourse(_Courses)

Course.readSpecificCourseInfo(_Courses, courseNum)
Course.updateSpecificCourseInfo(_Courses, courseNum)
Course.readCourse(_Courses)

examNum = int(input("Please enter exams number: "))
Exam.createExam(_Exams, examNum)
Exam.readExam(_Exams)

Exam.readSpecificExamInfo(_Exams, examNum)
Exam.updateSpecificExamInfo(_Exams, examNum)
Exam.readExam(_Exams)

studentNum = int(input("Please enter Students number: "))
Student.createStudent(_Students, studentNum)
Student.readStudent(_Students)

Student.readSpecificStudentInfo(_Students, studentNum)
Student.updateSpecificStudentInfo(_Students, studentNum)
Student.readStudent(_Students)


profNum = int(input("Please enter Professors number: "))
Professor.createProfessor(_Professors, profNum)
Professor.readProfessor(_Professors)

Professor.readSpecificProfessorInfo(_Professors, profNum)
Professor.updateSpecificProfessorInfo(_Professors, profNum)
Professor.readProfessor(_Professors)




print("Faculty Info: " + str(_Faculty))
print("Departments Info: " + str(_Departments))
print("Subjects Info: " + str(_Subjects))
print("Courses Info: " + str(_Courses))
print("Exams Info: " + str(_Exams))
print("Students Info: " + str(_Students))
print("Professors Info: " + str(_Professors))


