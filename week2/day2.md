## Create New Transaction

`begin;`

## Insert commands In Professors and Students tables

`INSERT INTO Professor(F_Name, L_Name, Age, Salary, Image, Faculty_id, Department_id) VALUES('Hossam', 'Khaled', 47, 40000.0, 'ashdg', 1, 26);`

`INSERT INTO Student(F_name, L_Name, F_phone, L_Phone, Birth_Date, Image, Age) VALUES('Mahmoud', 'Omar', 594653, 324985, 1991, 'sfss', 32);`

=====================================================================================

## Select commands of Professors and Students

`SELECT * FROM Professor;`
`SELECT * FROM Student;`


`When i open another session and select all the Professors and Students, the data was retrieved in the first session before i create the New Transaction will be shown in the second session`


=====================================================================================

## Delete commands of Professors with salary greater than 2000

```DELETE FROM Professor 
	WHERE SALARY > 20000;```


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

INSERT INTO Student(id, F_name, L_Name, F_phone, L_Phone, Birth_Date, Image, Age) VALUES(1, 'Mahmoud', 'Omar', 594653, 324985, 1991, 'sfss', 32);

`I will get an error when i try to insert commands in professors table with a duplicated id which is "current transaction is aborted, commands ignored until end of transaction block""`

=====================================================================================


## Final Commit command in the exercise

`When i commit, it shows me "ROLLBACK" message`


## Final Rollback command in the exercise
`When i rollback, it shows me a Warning which is "there is no transaction in progress" and Rollback work in the next line`




===============================================================================================================================================================================================================================================================



## "Join" exercise

`Select Subject.id, Name, Code, Duration from Subject INNER JOIN Course ON Course.Subject_id = Subject.id;`

`SELECT Subject.id, Name, Code, Duration, F_name, L_name FROM Subject INNER JOIN Course ON Course.Subject_id = Subject.id LEFT JOIN Professor ON Course.Professor_id = Professor.id;`

`SELECT Student.id, F_name, L_name, Line_1Address, Line_2Address FROM Student INNER JOIN Student_Address ON Student_Address.Student_id = Student.id INNER JOIN Address ON Student_Address.Address_id = Address.id;`

`SELECT Student.id, F_Name, L_Name, Duration from Student INNER JOIN Course_Enrolment ON Course_Enrolment.Student_id = Student.id INNER JOIN Course ON Course.id = Course_Enrolment.Course_id;`


## Another Solution for the 3rd Join quesion *solved with FULL OUTER JOIN"
 
`SELECT Student.id, F_name, L_name, Line_1Address, Line_2Address FROM Student FULL OUTER JOIN Student_Address ON Student_Address.Student_id = Student.id FULL OUTER JOIN Address ON Student_Address.Address_id = Address.id;`





















	


