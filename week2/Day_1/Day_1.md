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

============================================================================================

	Insert Into Address(Governorate, City, Line_1Address, Line_2Address)
		   Values('Giza', 'Giza', 'Faisal', null);
============================================================================================

	INSERT INTO Student(F_Name, L_Name, F_Phone, L_Phone, Birth_Date, Image)
	            VALUES('Ali', 'Mohamed', 09852121, 05496321, 25-10-1980, 'Hello');
	   
	INSERT INTO Student(F_Name, L_Name, F_Phone, L_Phone, Birth_Date, Image)
	            VALUES('Mahmoud', 'Omar', 321656, 846545, 1970, 'hi'),
	   	      	 ('Khaled', 'Mustafa', 94652, 321684, 1988, 'hello'),
			 ('Abdelrahman', 'Tarek', 3216, 65493, 1992, 'heyyy');
			 
	INSERT INTO Student(F_Name, L_Name, F_Phone, L_Phone, Birth_Date, Image)
	            VALUES('Mustafa', 'Mahmoud', 564321, 654962, 1995, 'hellooo');
============================================================================================

	INSERT INTO Professor(F_Name, L_Name, Age, Salary, Image, Faculty_id, Departement_id)
	   VALUES('Tarek', 'Mahmoud', 40, 20000.0, 'helloo', 1, 1), ('Salah', 'Ali', 37, 15000.0, 'hey', 1, 2),
	         ('Zain', 'Ahmed', 45, 30000.0, 'hii', 1, 3);
============================================================================================


	INSERT INTO Subject(Name, Code, Faculty_id, Department_id)
		VALUES('Programming Language', 'swe1', 1, 1), ('Algorithms and DS', 'swe2', 1, 1),
		('Software Engineering', 'swe3', 1, 1), ('Mathematics', 'swe4', 1, 2),
		('Business computer applications', 'swe5', 1, 2),
		('Information and internet technology', 'swe6', 1, 2),
		('Networking', 'swe7', 1, 3), ('Computer Graphics and Multimedia', 'swe8', 1, 3),
		('Data Mining', 'swe9', 1, 3);
============================================================================================
			
I	NSERT INTO Student_Address(Address_id, Student_id)
			VALUES(1,1), (14,2), (15,3), (16,4), (17,5), (18,8), (19,10), (20,11);
============================================================================================

	INSERT INTO Course(Duration, Subject_id, Professor_id)
		VALUES(2, 10, 1), (2, 11, 2), (3,12,3), (2,13,4), (6,14,5);
============================================================================================
			
	INSERT INTO Course_Enrolment(Course_id, Student_id)
		   VALUES(1,1), (2,2), (3,3), (4,4), (5,5);
============================================================================================

	INSERT INTO Exams(Date_Exam, Time_Exam, Duration, Course_id)
	   VALUES(2015, 8, 2, 6), (2016, 8, 2, 7), (2017, 8, 2, 8),
	         (2018, 8, 2, 9), (2019, 8, 2, 10);
```
			 
===============================================
## Select Data From Thse Tables.

```
SELECT * from Student;

 id |   f_name    | l_name  | f_phone | l_phone | birth_date |  image  
----+-------------+---------+---------+---------+------------+---------
  1 | Ali         | Mohamed | 9852121 | 5496321 | -1965      | Hello
  2 | Mahmoud     | Omar    |  321656 |  846545 | 1970       | hi
  3 | Khaled      | Mustafa |   94652 |  321684 | 1988       | hello
  4 | Abdelrahman | Tarek   |    3216 |   65493 | 1992       | heyyy
  5 | Mustafa     | Mahmoud |  564321 |  654962 | 1995       | hellooo
  6 | Ali         | Mohamed | 9852121 | 5496321 | -1965      | Hello
  7 | Mahmoud     | Omar    |  321656 |  846545 | 1970       | hi
  8 | Khaled      | Mustafa |   94652 |  321684 | 1988       | hello
  9 | Abdelrahman | Tarek   |    3216 |   65493 | 1992       | heyyy
 10 | Mustafa     | Mahmoud |  564321 |  654962 | 1995       | hellooo




SELECT * from Professor;

 id | f_name | l_name  | age | salary | image  | faculty_id | departement_id 
----+--------+---------+-----+--------+--------+------------+----------------
  1 | Tarek  | Mahmoud |  40 |  20000 | helloo |          1 |              1
  2 | Salah  | Ali     |  37 |  15000 | hey    |          1 |              2
  3 | Zain   | Ahmed   |  45 |  30000 | hii    |          1 |              3



SELECT * from Subject;

 id |                name                 | code | faculty_id | department_id 
----+-------------------------------------+------+------------+---------------
  1 | Programming Language                | swe1 |          1 |             1
  2 | Algorithms and DS                   | swe2 |          1 |             1
  3 | Software Engineering                | swe3 |          1 |             1
  4 | Mathematics                         | swe4 |          1 |             2
  5 | Business computer applications      | swe5 |          1 |             2
  6 | Information and internet technology | swe6 |          1 |             2
  7 | Networking                          | swe7 |          1 |             3
  8 | Computer Graphics and Multimedia    | swe8 |          1 |             3
  9 | Data Mining                         | swe9 |          1 |             3


	
SELECT * from Course;

  id | duration | subject_id | professor_id 
----+----------+------------+--------------
  6 |        2 |         10 |            1
  7 |        2 |         11 |            2
  8 |        3 |         12 |            3
  9 |        2 |         13 |            4
 10 |        6 |         14 |            5



SELECT * from Exams;

 id | date_exam | time_exam | duration | course_id 
----+-----------+-----------+----------+-----------
  6 |      2015 |         8 |        2 |         6
  7 |      2016 |         8 |        2 |         7
  8 |      2017 |         8 |        2 |         8
  9 |      2018 |         8 |        2 |         9
 10 |      2019 |         8 |        2 |        10



SELECT * from Department;

 id | name | faculty_id 
----+------+------------
  1 | CS   |          1
  2 | IS   |          1
  3 | IT   |          1




Select * from Professor where Age =40; 

 id | f_name | l_name  | age | salary | image  | faculty_id | departement_id 
----+--------+---------+-----+--------+--------+------------+----------------
  1 | Tarek  | Mahmoud |  40 |  20000 | helloo |          1 |              1
      


SELECT * from Professor where Salary > 10000;

 id | f_name | l_name  | age | salary | image  | faculty_id | departement_id 
----+--------+---------+-----+--------+--------+------------+----------------
  1 | Tarek  | Mahmoud |  40 |  20000 | helloo |          1 |              1
  2 | Salah  | Ali     |  37 |  15000 | hey    |          1 |              2
  3 | Zain   | Ahmed   |  45 |  30000 | hii    |          1 |              3



SELECT * from Professor ORDER BY Salary;

 id | f_name | l_name  | age | salary | image  | faculty_id | departement_id 
----+--------+---------+-----+--------+--------+------------+----------------
  2 | Salah  | Ali     |  37 |  15000 | hey    |          1 |              2
  1 | Tarek  | Mahmoud |  40 |  20000 | helloo |          1 |              1
  3 | Zain   | Ahmed   |  45 |  30000 | hii    |          1 |              3



SELECT * from Student ORDER BY Birth_Date;

 id |   f_name    | l_name  | f_phone | l_phone | birth_date |  image  
----+-------------+---------+---------+---------+------------+---------
  1 | Ali         | Mohamed | 9852121 | 5496321 | -1965      | Hello
  6 | Ali         | Mohamed | 9852121 | 5496321 | -1965      | Hello
  2 | Mahmoud     | Omar    |  321656 |  846545 | 1970       | hi
  7 | Mahmoud     | Omar    |  321656 |  846545 | 1970       | hi
  3 | Khaled      | Mustafa |   94652 |  321684 | 1988       | hello
  8 | Khaled      | Mustafa |   94652 |  321684 | 1988       | hello
  9 | Abdelrahman | Tarek   |    3216 |   65493 | 1992       | heyyy
  4 | Abdelrahman | Tarek   |    3216 |   65493 | 1992       | heyyy
  5 | Mustafa     | Mahmoud |  564321 |  654962 | 1995       | hellooo
 10 | Mustafa     | Mahmoud |  564321 |  654962 | 1995       | hellooo



SELECT *, AVG(Salary)
	FROM Professor
	GROUP BY id;
	
 id | f_name | l_name  | age | salary | image  | faculty_id | departement_id |  avg  
----+--------+---------+-----+--------+--------+------------+----------------+-------
  2 | Salah  | Ali     |  37 |  15000 | hey    |          1 |              2 | 15000
  1 | Tarek  | Mahmoud |  40 |  20000 | helloo |          1 |              1 | 20000
  3 | Zain   | Ahmed   |  45 |  30000 | hii    |          1 |              3 | 30000




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
