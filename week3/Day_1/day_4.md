##Exersice1_Solution

```
CREATE TABLE IF NOT EXISTS PERSON(
	id serial PRIMARY KEY,
	email varchar(40) CHECK(LOWER(email) = email)
);


INSERT INTO PERSON(email) VALUES('hello@gmail.com');
INSERT INTO PERSON(email) VALUES('hello@gmail.com'), ('hello@gmail.com'), ('hiii@gmail.com'),
		('hello@gmail.com'), ('yoo@gmail.com'), ('hello@gmail.com');
		
		
 id |      email       
----+------------------
  1 | john@example.com
  2 | john@example.com
  3 | bob@example.com
  4 | john@example.com
  5 | john@example.com
  6 | john@example.com



		


SELECT email, COUNT(email) FROM PERSON GROUP BY email;



      email       | count 
------------------+-------
 bob@example.com  |     1
 john@example.com |     5





 DELETE FROM PERSON
 	WHERE id IN(SELECT id FROM(SELECT id, ROW_NUMBER() OVER(PARTITION BY email ORDER BY id)
 	AS row_num FROM PERSON) T WHERE T.row_num > 1);
 	
 	
 	
 id |      email       
----+------------------
  1 | john@example.com
  3 | bob@example.com


```

==============================================================================================

##Another Soltion
```
DELETE FROM PERSON a USING PERSON b 
	WHERE a.id > b.id AND a.email = b.email AND a.email = 'hello@gmail.com';
	
 id |      email       
----+------------------
  1 | john@example.com
  3 | bob@example.com


	
```
