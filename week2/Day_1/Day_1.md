## Create a SQL database for the Above ER diagram.

```
 * >>> - Faculty Table:
 
	create table if not exists Faculty(
		id serial primary key ,
	    name varchar(60) not null
	);
	
 * >>> - Department Table:
 
	create table if not exists Department(
		id serial primary key ,
	    name varchar(60) not null,
		Faculty_id int references Faculty (id)
	);
	
 * >>> - Address Table:
 
	create table if not exists Address(
		id serial primary key,
		Governorate varchar(60) not null,
	    City varchar(60) not null,
		line_1Address varchar(80) not null,
		line_2Address varchar(80) not null
	);
	
 * >>> - Student Table:

	create table if not exists Student(
		id serial primary key,
		F_Name varchar(40) not null,
		L_Name varchar(40) not null,
		F_Phone int not null,
		L_Phone int not null,
		Birth_Date varchar(30) not null,
		Image varchar(30) not null
	);
	
 * >>> - Student_Address Table:
 
	create table if not exists Student_Address(
		id serial primary key,
		
		Address_id int references Address (id),
		Student_id int references Student (id)
	);
	
 * >>> - Professor Table:
 
	create table if not exists Professor(
		id serial primary key,
		F_Name varchar(40) not null,
		L_Name varchar(40) not null,
		Age int not null,
		Salary float not null,
		Image varchar(30) not null,
		Faculty_id int references Faculty (id),
		Departement_id int references Departement (id)
		
	);
	
 * >>> - Subject Table:
 
	create table if not exists Subject(
		id serial primary key,
		Name varchar(60) not null,
		Code varchar(40) not null unique,
		Faculty_id int references Faculty (id),
		Department_id int references Department(id)
	);
	
 * >>> - Course Table:
 
	create table if not exists Course(
		id serial primary key,
		Duration int not null,
		Subject_id int references Subject (id),
		Professor_id int references Professor (id)
			
	);
	
 * >>> - Course_Enrolment Table:
 
	create table if not exists Course_Enrolment(
		id serial primary key,
		Course_id int references Course (id),
		Student_id int references Student (id)
	);
	
 * >>> - Exams Table:
 
	create table if not exists Exams(
		id serial primary key,
		Date_Exam int not null,
		Time_Exam int not null,
		Duration int not null,
		Course_id int references Course (id)
	);

```

===================================================================================================================
## Insert Data Into These Tables.

```
	INSERT INTO Faculty(name) VALUES('Computers and Information Technology');

============================================================================================

	INSERT INTO Department(name, Faculty_id) VALUES('CS', 1), ('IS', 1), ('IT',1);

	 Delete from Department
	 	Where id IN(1,2,3);
============================================================================================

	Insert Into Address(Governorate, City, Line_1Address, Line_2Address)
		   Values('Giza', 'Giza', 'Faisal', null);
============================================================================================

	INSERT INTO Student(F_Name, L_Name, Birth_Date, Image, Age)
		   VALUES('Ali', 'Mohamed', 25-10-1980, 'Hello', 22);
		   
	INSERT INTO Student(F_Name, L_Name, Birth_Date, Image, Age)
		   VALUES('Mahmoud', 'Omar', 1970, 'hi', 22),
		   		 ('Khaled', 'Mustafa', 1988, 'hello', 22),
				 ('Abdelrahman', 'Tarek', 1992, 'heyyy', 22);
				 
	INSERT INTO Student(F_Name, L_Name, Birth_Date, Image, Age)
		   VALUES('Mustafa', 'Mahmoud', 1995, 'hellooo', 22);
		   
	INSERT INTO Student(F_Name, L_Name, F_Phone, L_Phone, Birth_Date, Image, Age)
		   VALUES('Omar', 'Mustafa', 1977, 'hellooo', 22);
		   
	INSERT INTO Student(F_Name, L_Name, F_Phone, L_Phone, Birth_Date, Image, Age)
		   VALUES('Ahmed', 'Hossam', 1991, 'sfss', 32);
		   
	INSERT INTO Student(F_Name, L_Name, F_Phone, L_Phone, Birth_Date, Image, Age)
		   VALUES('Amr', 'Emad', 1991, 'heey', 32);
============================================================================================

	INSERT INTO Professor(F_Name, L_Name, Age, Salary, Image)
		   VALUES('Karem', 'Mousa', 25, 5000.0, 'Hi');
		   
	INSERT INTO Professor(F_Name, L_Name, Age, Salary, Image)
		   VALUES('Tarek', 'Mahmoud', 40, 20000.0, 'helloo'), ('Salah', 'Ali', 37, 15000.0, 'hey'),
			 ('Zain', 'Ahmed', 45, 30000.0, 'hii'), ('Omar', 'Fakhry', 47, 35000.0, 'hellooo');
	INSERT INTO Professor(F_Name, L_Name, Age, Salary, Image) 
		   VALUES('Hosny', 'Hassan', 42, 35000.0, 'heyyy');
============================================================================================


	INSERT INTO Subject(Name, Code, Faculty_id, Department_id)
			VALUES('Programming Language', 'swe1', 1, 25), ('Algorithms and DS', 'swe2', 1, 25),
			('Software Engineering', 'swe3', 1, 25), ('Mathematics', 'swe4', 1, 26),
			('Business computer applications', 'swe5', 1, 26),
			('Information and internet technology', 'swe6', 1, 26),
			('Networking', 'swe7', 1, 27), ('Computer Graphics and Multimedia', 'swe8', 1, 27),
			('Data Mining', 'swe9', 1, 27);
============================================================================================
			
I	NSERT INTO Student_Address(Address_id, Student_id)
			VALUES(1,1), (14,2), (15,3), (16,4), (17,5), (18,8), (19,10), (20,11);
============================================================================================

	INSERT INTO Course(Duration, Subject_id, Professor_id)
			VALUES(2, 1, 1), (2, 2, 2), (3,3,3), (2,4,4), (6,5,5);
============================================================================================
			
	INSERT INTO Course_Enrolment(Course_id, Student_id)
		   VALUES(1,1), (2,2), (3,3), (4,4), (5,5);
============================================================================================

	INSERT INTO Exams(Date_Exam, Time_Exam, Duration, Course_id)
		   VALUES(2015, 8, 2, 1), (2016, 8, 2, 2), (2017, 8, 2, 3),
			 (2018, 8, 2, 4), (2019, 8, 2, 5);
	         
```
			 
===============================================
## Select Data From Thse Tables.

```
SELECT * from Student;

 id |   f_name    | l_name  | birth_date |    image     | age 
----+-------------+---------+------------+--------------+-----
  1 | Ali         | Mohamed |      -1965 | \x48656c6c6f | 22
  2 | Mahmoud     | Omar    |       1970 | hi           | 22
  3 | Khaled      | Mustafa |       1988 | hello        | 22
  4 | Abdelrahman | Tarek   |       1992 | heyyy        | 22
  5 | Mustafa     | Mahmoud |       1995 | hellooo      | 22
  8 | Omar        | Mustafa |       1977 | blabla       | 22
 10 | Ahmed       | Hosaam  |       1991 | sfss         | 32
 11 | Amr         | Emad    |       1991 | heey         | 32



SELECT * from Professor;

	 id | age | salary |  image  | faculty_id | department_id | course_id 
----+-----+--------+---------+------------+---------------+-----------
  1 |  25 |   5000 | Hi      |            |               |          
  2 |  40 |  20000 | helloo  |            |               |          
  3 |  37 |  20000 | hey     |            |               |          
  4 |  45 |  20000 | hii     |            |               |          
  5 |  47 |  20000 | hellooo |            |               |          
 11 |  37 |  30000 | sghfsh  |          1 |            25 |         1
 13 |  47 |  40000 | ashdg   |          1 |            26 |         2


SELECT * from Subject;

 id |                name                 | code | faculty_id | department_id 
----+-------------------------------------+------+------------+---------------
  1 | Programming Language                | swe1 |          1 |            25
  2 | Algorithms and DS                   | swe2 |          1 |            25
  3 | Software Engineering                | swe3 |          1 |            25
  4 | Mathematics                         | swe4 |          1 |            26
  5 | Business computer applications      | swe5 |          1 |            26
  6 | Information and internet technology | swe6 |          1 |            26
  7 | Networking                          | swe7 |          1 |            27
  8 | Computer Graphics and Multimedia    | swe8 |          1 |            27
  9 | Data Mining                         | swe9 |          1 |            27

	
SELECT * from Course;

 id | duration | subject_id | professor_id 
----+----------+------------+--------------
  1 |        2 |          1 |            1
  2 |        2 |          2 |            2
  3 |        3 |          3 |            3
  4 |        2 |          4 |            4
  5 |        6 |          5 |            5


SELECT * from Exams;

 id | date_exam | time_exam | duration | course_id 
----+-----------+-----------+----------+-----------
  1 |      2015 |         8 |        2 |         1
  2 |      2016 |         6 |        2 |         2
  3 |      2017 |         5 |        2 |         3
  4 |      2018 |         4 |        2 |         4
  5 |      2019 |         3 |        2 |         5


SELECT * from Department;

 id | name | faculty_id 
----+------+------------
 25 | CS   |          1
 26 | IS   |          1
 27 | IT   |          1



Select * from Professor where Age =40; 

 id | age | salary | image  | faculty_id | department_id | course_id 
----+-----+--------+--------+------------+---------------+-----------
  2 |  40 |  20000 | helloo |            |               |          


SELECT * from Professor where Salary > 10000;

	 id | age | salary |  image  | faculty_id | department_id | course_id 
----+-----+--------+---------+------------+---------------+-----------
  2 |  40 |  20000 | helloo  |            |               |          
  3 |  37 |  20000 | hey     |            |               |          
  4 |  45 |  20000 | hii     |            |               |          
  5 |  47 |  20000 | hellooo |            |               |          
 11 |  37 |  30000 | sghfsh  |          1 |            25 |         1
 13 |  47 |  40000 | ashdg   |          1 |            26 |         2


SELECT * from Professor ORDER BY Salary;

 id | age | salary |  image  | faculty_id | department_id | course_id 
----+-----+--------+---------+------------+---------------+-----------
  1 |  25 |   5000 | Hi      |            |               |          
  2 |  40 |  20000 | helloo  |            |               |          
  3 |  37 |  20000 | hey     |            |               |          
  4 |  45 |  20000 | hii     |            |               |          
  5 |  47 |  20000 | hellooo |            |               |          
 11 |  37 |  30000 | sghfsh  |          1 |            25 |         1
 13 |  47 |  40000 | ashdg   |          1 |            26 |         2


SELECT * from Student ORDER BY Birth_Date;

 id |   f_name    | l_name  | birth_date |    image     | age 
----+-------------+---------+------------+--------------+-----
  1 | Ali         | Mohamed |      -1965 | \x48656c6c6f | 22
  2 | Mahmoud     | Omar    |       1970 | hi           | 22
  8 | Omar        | Mustafa |       1977 | blabla       | 22
  3 | Khaled      | Mustafa |       1988 | hello        | 22
 11 | Amr         | Emad    |       1991 | heey         | 32
 10 | Ahmed       | Hosaam  |       1991 | sfss         | 32
  4 | Abdelrahman | Tarek   |       1992 | heyyy        | 22
  5 | Mustafa     | Mahmoud |       1995 | hellooo      | 22


SELECT *, AVG(Salary)
	FROM Professor
	GROUP BY id;
	
	 id | age | salary |  image  | faculty_id | department_id | course_id |  avg  
----+-----+--------+---------+------------+---------------+-----------+-------
  4 |  45 |  20000 | hii     |            |               |           | 20000
 13 |  47 |  40000 | ashdg   |          1 |            26 |         2 | 40000
  2 |  40 |  20000 | helloo  |            |               |           | 20000
 11 |  37 |  30000 | sghfsh  |          1 |            25 |         1 | 30000
  3 |  37 |  20000 | hey     |            |               |           | 20000
  5 |  47 |  20000 | hellooo |            |               |           | 20000
  1 |  25 |   5000 | Hi      |            |               |           |  5000



	UPDATE Professor
		SET Salary = 20000 Where Salary > 10000;
	DELETE FROM Professor
		Where Salary > 20000;
	
```
	
	
===================================================================================================================
## Update These Tables

```

	ALTER TABLE Student
		ADD COLUMN Age VARCHAR;
		
	UPDATE Student
		SET Age =22
		Where id =1;
		
	UPDATE Student
		SET Age =22
		Where id =2;
		
	UPDATE Student
		SET Age =22
		Where id =3;
		
	UPDATE Student
		SET Age =22
		Where id =4;
		
	UPDATE Student
		SET Age =22
		Where id =5;
		
	UPDATE Exams
		SET Time_Exam = 6
		Where id = 2;
		
	UPDATE Exams
		SET Time_Exam = 5
		Where id = 3;
		
	UPDATE Exams
		SET Time_Exam = 4
		Where id = 4;
		
	UPDATE Exams
		SET Time_Exam = 3
		Where id = 5;
	
```




===============================================================================================



https://pgexercises.com/questions/basic/selectall.html
##Solution:
select * from cd.facilities;




https://pgexercises.com/questions/basic/selectspecific.html
##Solution:
select name, membercost from cd.facilities



https://pgexercises.com/questions/basic/where.html
##Solution:
select * from cd.facilities where membercost > 0;



https://pgexercises.com/questions/basic/where2.html
##Solution:
select facid, name, membercost, monthlymaintenance from cd.facilities where membercost > 0 and membercost < monthlymaintenance/50;
