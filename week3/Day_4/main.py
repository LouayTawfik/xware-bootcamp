from college import Faculty, Department, Subject, Course, Exam, Student, Professor



_Faculty = []
_Departments = []
_Subjects = []
_Courses = []
_Exams = []
_Students = []
_Professors = []


Faculty.createFaculty(_Faculty)

print("Faculty before update...")
Faculty.readFaculty(_Faculty)

Faculty.updateFaculty(_Faculty)

print("Faculty after update...")
Faculty.readFaculty(_Faculty)

#====================================================================

depNum = int(input("Please enter department numbers: "))
Department.createDepartment(_Departments, depNum)

print("Departments before update...")
Department.readDepartment(_Departments)

Department.readSpecificDep(_Departments, depNum)

Department.updateSpecificDepInfo(_Departments, depNum)

print("Departments after update...")
Department.readDepartment(_Departments)

#====================================================================

subNum = int(input("Please enter subject numbers: "))
Subject.createSubject(_Subjects, subNum)

print("Subjects before update...")
Subject.readSubject(_Subjects)

Subject.readSpecificSubjectInfo(_Subjects, subNum)

Subject.updateSpecificSubInfo(_Subjects, subNum)

print("Subjects after update...")
Subject.readSubject(_Subjects)

#====================================================================

courseNum = int(input("Please enter course numbers: "))
Course.createCourse(_Courses, courseNum)

print("Courses before update...")
Course.readCourse(_Courses)

Course.readSpecificCourseInfo(_Courses, courseNum)

Course.updateSpecificCourseInfo(_Courses, courseNum)

print("Courses after update...")
Course.readCourse(_Courses)

#====================================================================

examNum = int(input("Please enter exams number: "))
Exam.createExam(_Exams, examNum)

print("Exams before update...")
Exam.readExam(_Exams)

Exam.readSpecificExamInfo(_Exams, examNum)

Exam.updateSpecificExamInfo(_Exams, examNum)

print("Exams after update...")
Exam.readExam(_Exams)

#====================================================================

studentNum = int(input("Please enter Students number: "))
Student.createStudent(_Students, studentNum)

print("Students before update...")
Student.readStudent(_Students)

Student.readSpecificStudentInfo(_Students, studentNum)

Student.updateSpecificStudentInfo(_Students, studentNum)

print("Exams after update...")
Student.readStudent(_Students)

#====================================================================

profNum = int(input("Please enter Professors number: "))
Professor.createProfessor(_Professors, profNum)

print("Professors before update...")
Professor.readProfessor(_Professors)

Professor.readSpecificProfessorInfo(_Professors, profNum)

Professor.updateSpecificProfessorInfo(_Professors, profNum)

print("Professors after update...")
Professor.readProfessor(_Professors)


#====================================================================

print("Faculty Info: " + str(_Faculty))
print("Departments Info: " + str(_Departments))
print("Subjects Info: " + str(_Subjects))
print("Courses Info: " + str(_Courses))
print("Exams Info: " + str(_Exams))
print("Students Info: " + str(_Students))
print("Professors Info: " + str(_Professors))


#==========================================================

Faculty.readFaculty_Professor(_Faculty, _Professors)
Faculty.readFaculty_Department(_Faculty, _Departments)
Professor.readProfessor_Subject(_Professors, _Subjects)
Professor.readProfessor_Course(_Professors, _Courses)




            


