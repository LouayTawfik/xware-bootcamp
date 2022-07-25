create table if not exists Faculty(
	id serial primary key ,
    name varchar(60) not null
);
create table if not exists Department(
	id serial primary key ,
    name varchar(60) not null,
	Faculty_id int references Faculty (id)
);
create table if not exists Address(
	id serial primary key,
	Governorate varchar(60) not null,
    City varchar(60) not null,
	line_1Address varchar(80) not null,
	line_2Address varchar(80) not null
);
create table if not exists Student(
	id serial primary key,
	F_Name varchar(40) not null,
	L_Name varchar(40) not null,
	F_Phone int not null,
	L_Phone int not null,
	Birth_Date varchar(30) not null,
	Image varchar(30) not null
);
create table if not exists Student_Address(
	id serial primary key,
	
	Address_id int references Address (id),
	Student_id int references Student (id)
);
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
create table if not exists Subject(
	id serial primary key,
	Name varchar(60) not null,
	Code varchar(40) not null unique,
	Faculty_id int references Faculty (id),
	Department_id int references Department(id)
);
create table if not exists Course(
	id serial primary key,
	Duration int not null,
	Subject_id int references Subject (id),
	Professor_id int references Professor (id)
		
);
create table if not exists Course_Enrolment(
	id serial primary key,
	Course_id int references Course (id),
	Student_id int references Student (id)
);
create table if not exists Exams(
	id serial primary key,
	Date_Exam int not null,
	Time_Exam int not null,
	Duration int not null,
	Course_id int references Course (id)
);

-- ============================================
-- Insert Data:-
INSERT INTO Faculty(name) VALUES('Computers and Information Technology');
INSERT INTO Department(name, Faculty_id) VALUES('CS', 1), ('IS', 1), ('IT',1);
Insert Into Address(Governorate, City, Line_1Address, Line_2Address)
	   Values('Giza', 'Giza', 'Faisal', null);
INSERT INTO Student(F_Name, L_Name, F_Phone, L_Phone, Birth_Date, Image)
	   VALUES('Ali', 'Mohamed', 09852121, 05496321, 25-10-1980, 'Hello');
	   
INSERT INTO Student(F_Name, L_Name, F_Phone, L_Phone, Birth_Date, Image)
	   VALUES('Mahmoud', 'Omar', 321656, 846545, 1970, 'hi'),
	   		 ('Khaled', 'Mustafa', 94652, 321684, 1988, 'hello'),
			 ('Abdelrahman', 'Tarek', 3216, 65493, 1992, 'heyyy');
			 
INSERT INTO Student(F_Name, L_Name, F_Phone, L_Phone, Birth_Date, Image)
	   VALUES('Mustafa', 'Mahmoud', 564321, 654962, 1995, 'hellooo');
			 


INSERT INTO Professor(F_Name, L_Name, Age, Salary, Image)
	   VALUES('Karem', 'Mousa', 25, 5000.0, 'Hi');
INSERT INTO Professor(F_Name, L_Name, Age, Salary, Image)
	   VALUES('Tarek', 'Mahmoud', 40, 20000.0, 'helloo'), ('Salah', 'Ali', 37, 15000.0, 'hey'),
	         ('Zain', 'Ahmed', 45, 30000.0, 'hii'), ('Omar', 'Fakhry', 47, 35000.0, 'hellooo');
INSERT INTO Professor(F_Name, L_Name, Age, Salary, Image) 
	   VALUES('Hosny', 'Hassan', 42, 35000.0, 'heyyy');
-- Delete from Department
-- 	Where id IN(1,2,3);

INSERT INTO Subject(Name, Code, Faculty_id, Department_id)
		VALUES('Programming Language', 'swe1', 1, 25), ('Algorithms and DS', 'swe2', 1, 25),
		('Software Engineering', 'swe3', 1, 25), ('Mathematics', 'swe4', 1, 26),
		('Business computer applications', 'swe5', 1, 26),
		('Information and internet technology', 'swe6', 1, 26),
		('Networking', 'swe7', 1, 27), ('Computer Graphics and Multimedia', 'swe8', 1, 27),
		('Data Mining', 'swe9', 1, 27);
		
INSERT INTO Student_Address(Address_id, Student_id)
		VALUES(1,1);
		
Drop Table Course Cascade;
Select * from Exams;
INSERT INTO Course(Duration, Subject_id, Professor_id)
		VALUES(2, 1, 1), (2, 2, 2), (3,3,3), (2,4,4), (6,5,5);
		
INSERT INTO Course_Enrolment(Course_id, Student_id)
	   VALUES(1,1), (2,2), (3,3), (4,4), (5,5);
	   
INSERT INTO Exams(Date_Exam, Time_Exam, Duration, Course_id)
	   VALUES(2015, 8, 2, 1), (2016, 8, 2, 2), (2017, 8, 2, 3),
	         (2018, 8, 2, 4), (2019, 8, 2, 5);
			 
-- ===============================================
-- Select Data

SELECT * from Student;
SELECT * from Professor;
SELECT * from Subject;
SELECT * from Course;
SELECT * from Exams;
SELECT * from Department;


Select * from Professor where Age =40; 
SELECT * from Professor where Salary > 10000;
SELECT * from Professor ORDER BY Salary;
SELECT * from Student ORDER BY Birth_Date;
SELECT AVG(Salary)
	FROM Professor;
UPDATE Professor
	SET Salary = 20000 Where Salary > 10000;
DELETE FROM Professor
	Where Salary > 20000;
	
	
	
	
-- ==============================================
-- Update Data

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
	

	

	
































