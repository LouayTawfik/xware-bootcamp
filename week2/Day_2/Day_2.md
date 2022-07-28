## Create New Transaction

`begin;`

## Insert commands In Professors and Students tables

`INSERT INTO Professor(F_Name, L_Name, Age, Salary, Image, Faculty_id, Department_id) VALUES('Hossam', 'Khaled', 47, 40000.0, 'ashdg', 1, 26);`

`INSERT INTO Student(F_name, L_Name, F_phone, L_Phone, Birth_Date, Image, Age) VALUES('Mahmoud', 'Omar', 594653, 324985, 1991, 'sfss', 32);`

=====================================================================================

## Select commands of Professors and Students

```

SELECT * FROM Professor;

 id | age | salary |  image  | faculty_id | department_id | course_id 
----+-----+--------+---------+------------+---------------+-----------
  1 |  25 |   5000 | Hi      |            |               |          
  2 |  40 |  20000 | helloo  |            |               |          
  3 |  37 |  20000 | hey     |            |               |          
  4 |  45 |  20000 | hii     |            |               |          
  5 |  47 |  20000 | hellooo |            |               |          
 11 |  37 |  30000 | sghfsh  |          1 |            25 |         1
 13 |  47 |  40000 | ashdg   |          1 |            26 |         2



SELECT * FROM Student;

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


When i open another session and select all the Professors and Students, the data was retrieved in the first session before i create the New Transaction will be shown in the second session

```
=====================================================================================

## Delete commands of Professors with salary greater than 2000

<!--DELETE FROM Professor 
	WHERE SALARY > 20000; -->


`Nothing will change when i try to select all Professors and Students in the other session`


## Rollback command

`ROLLBACK;`

`Nothing will change when i try to select all Professors and Students in the other session`


## Commit command

`COMMIT;`

`When i select all professors and students in the other session after i commit in the first session the same result will be shown in the other session as i select all professors and students in the first session`

=====================================================================================

## Insert commands in professors table with a duplicated id

`INSERT INTO Professor(id, F_Name, L_Name, Age, Salary, Image, Faculty_id, Department_id) VALUES(1, 'Hossam', 'Khaled', 47, 40000.0, 'ashdg', 1, 26);`

`I will get an error when i try to insert commands in professors table with a duplicated id which is "duplicate key value violates unique constraint "professor_pkey""`


## Insert commands in student table with a duplicated id

`INSERT INTO Student(id, F_name, L_Name, F_phone, L_Phone, Birth_Date, Image, Age) VALUES(1, 'Mahmoud', 'Omar', 594653, 324985, 1991, 'sfss', 32);`

`I will get an error when i try to insert commands in professors table with a duplicated id which is "current transaction is aborted, commands ignored until end of transaction block""`

=====================================================================================


## Final Commit command in the exercise

`When i commit, it shows me "ROLLBACK" message`


## Final Rollback command in the exercise
`When i rollback, it shows me a Warning which is "there is no transaction in progress" and Rollback work in the next line`




===============================================================================================================================================================================================================================================================



## "Join" exercise

```
Select Subject.id, Name, Code, Duration from Subject INNER JOIN Course ON Course.Subject_id = Subject.id;

 id |              name              | code | duration 
----+--------------------------------+------+----------
  1 | Programming Language           | swe1 |        2
  2 | Algorithms and DS              | swe2 |        2
  3 | Software Engineering           | swe3 |        3
  4 | Mathematics                    | swe4 |        2
  5 | Business computer applications | swe5 |        6




SELECT Subject.id, Name, Code, Duration, F_name, L_name FROM Subject INNER JOIN Course ON Course.Subject_id = Subject.id LEFT JOIN Professor ON Course.Professor_id = Professor.id;

 id |         name         | code | duration | f_name | l_name  
----+----------------------+------+----------+--------+---------
  1 | Programming Language | swe1 |        2 | Tarek  | Mahmoud
  2 | Algorithms and DS    | swe2 |        2 | Salah  | Ali
  3 | Software Engineering | swe3 |        3 | Zain   | Ahmed



SELECT Student.id, F_name, L_name, Line_1Address, Line_2Address FROM Student INNER JOIN Student_Address ON Student_Address.Student_id = Student.id INNER JOIN Address ON Student_Address.Address_id = Address.id;

 id |   f_name    | l_name  | line_1address | line_2address 
----+-------------+---------+---------------+---------------
  1 | Ali         | Mohamed | Faisal        | 
  2 | Mahmoud     | Omar    | asjha         | sfsf
  3 | Khaled      | Mustafa | sfa           | asfw
  4 | Abdelrahman | Tarek   | hfjsf         | efef
  5 | Mustafa     | Mahmoud | hgsf          | jksds
  6 | Ali         | Mohamed | jksf          | sfs
  7 | Mahmoud     | Omar    | sdas          | sjsd
  8 | Khaled      | Mustafa | jsfsf         | jashdka
  9 | Abdelrahman | Tarek   | jbfs          | sjkfhs
 10 | Mustafa     | Mahmoud | sfg           | suih


SELECT Student.id, F_Name, L_Name, Duration from Student INNER JOIN Course_Enrolment ON Course_Enrolment.Student_id = Student.id INNER JOIN Course ON Course.id = Course_Enrolment.Course_id;

 id | f_name  | l_name  | duration 
----+---------+---------+----------
  1 | Ali     | Mohamed |        2
  2 | Mahmoud | Omar    |        2
  3 | Khaled  | Mustafa |        3



```


## Another Solution for the 3rd Join quesion *solved with FULL OUTER JOIN"
 
```
SELECT Student.id, F_name, L_name, Line_1Address, Line_2Address FROM Student FULL OUTER JOIN Student_Address ON Student_Address.Student_id = Student.id FULL OUTER JOIN Address ON Student_Address.Address_id = Address.id;

 id |   f_name    | l_name  | line_1address | line_2address 
----+-------------+---------+---------------+---------------
  1 | Ali         | Mohamed | Faisal        | 
  2 | Mahmoud     | Omar    | asjha         | sfsf
  3 | Khaled      | Mustafa | sfa           | asfw
  4 | Abdelrahman | Tarek   | hfjsf         | efef
  5 | Mustafa     | Mahmoud | hgsf          | jksds
  6 | Ali         | Mohamed | jksf          | sfs
  7 | Mahmoud     | Omar    | sdas          | sjsd
  8 | Khaled      | Mustafa | jsfsf         | jashdka
  9 | Abdelrahman | Tarek   | jbfs          | sjkfhs
 10 | Mustafa     | Mahmoud | sfg           | suih



```




















	


