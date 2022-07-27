## Exercise 1_ Normalize Student and Professor

```

create table if not exists Student_Phone(
	id serial primary key,
	F_Phone int not null,
	L_Phone int not null,
	
	Student_id int references Student(id)
);




 id | f_phone | l_phone | student_id 
----+---------+---------+------------
  1 |  654365 |  984654 |          1
  2 |   56432 |   89465 |          2
  3 |   84654 |   65432 |          3
  4 |   54532 |    6542 |          4
  5 |    5612 |   56125 |          5
  6 |   56122 |   89465 |          8
  7 |   56432 |   56452 |         10
  8 |  656532 |  846521 |         11








create table if not exists Professor_Name(
	id serial primary key,
	F_Name varchar(40),
	L_Name varchar(40),
	
	Professor_id int references Professor(id)
);





 id | f_name  | l_name  | professor_id 
----+---------+---------+--------------
  1 | Hamada  | Hassan  |            1
  2 | Hossam  | Ali     |            2
  3 | Mustafa | Hussein |            3
  4 | Khaled  | Omar    |            4
  5 | Ahmed   | Ali     |            5
  6 | Mahmoud | Ismael  |           11
  7 | Amr     | Mustafa |           13


```

==================================================================


## Exercise 2:-





```

create table if not exists Person(
	personId serial primary key,
	lastName  varchar(50),
	firstName varchar(50)
);



 personid | lastname | firstname 
----------+----------+-----------
        1 | Wang     | Allen
        2 | Alice    | Bob
        3 | Smith    | Lee





create table if not exists Address(
	addressId serial primary key,
	city varchar(40),
	state varchar(40),
	
	Person_id int references Person(personId)
);



 addressid |     city      |   state    | personid 
-----------+---------------+------------+----------
         1 | New York City | New York   |        2
         2 | Leetcode      | California |        1






```




## INSERT steps


`INSERT INTO Person(lastName, firstName) VALUES('Wang', 'Allen'), ('Alice', 'Bob');`

`INSERT INTO Address(personId, city, state) VALUES(2, 'New York City', 'New York'), (1, 'Leetcode', 'California');`

`INSERT INTO Person(lastName, firstName) VALUES('Smith', 'Lee');`



## JOIN steps

`SELECT Person.firstName, lastName, city, state FROM Person FULL OUTER JOIN Address ON Address.personId = Person.personId;`

```
 firstname | lastname |     city      |   state
-----------+----------+---------------+------------
 Bob       | Alice    | New York City | New York
 Allen     | Wang     | Leetcode      | California
 Lee       | Smith    |               | 



```



