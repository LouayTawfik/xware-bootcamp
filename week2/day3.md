## Exercise 1_ Normalize Student and Professor

`create table if not exists Student_Phone(
	id serial primary key,
	F_Phone int not null,
	L_Phone int not null,
	
	Student_id int references Student(id)
);`




`create table if not exists Professor_Name(
	id serial primary key,
	F_Name varchar(40),
	L_Name varchar(40),
	
	Professor_id int references Professor(id)
);`

==================================================================


## Exercise 2:-

`create table if not exists Person(
	personId serial primary key,
	lastName  varchar(50),
	firstName varchar(50)
);`




`create table if not exists Address(
	addressId serial primary key,
	city varchar(40),
	state varchar(40),
	
	Person_id int references Person(personId)
);`



## INSERT steps


`INSERT INTO Person(lastName, firstName) VALUES('Wang', 'Allen'), ('Alice', 'Bob');`

`INSERT INTO Address(personId, city, state) VALUES(2, 'New York City', 'New York'), (1, 'Leetcode', 'California');`

`INSERT INTO Person(lastName, firstName) VALUES('Smith', 'Lee');`



## JOIN steps

`SELECT Person.firstName, lastName, city, state FROM Person FULL OUTER JOIN Address ON Address.personId = Person.personId;`






