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
----+-----------------
  1 | hello@gmail.com
  2 | hello@gmail.com
  3 | hello@gmail.com
  4 | hiii@gmail.com
  5 | hello@gmail.com
  6 | yoo@gmail.com
  7 | hello@gmail.com

		


SELECT email, COUNT(email) FROM PERSON GROUP BY email;



      email      | count 
-----------------+-------
 hello@gmail.com |     5
 yoo@gmail.com   |     1
 hiii@gmail.com  |     1



 DELETE FROM PERSON
 	WHERE id IN(SELECT id FROM(SELECT id, ROW_NUMBER() OVER(PARTITION BY email ORDER BY id)
 	AS row_num FROM PERSON) T WHERE T.row_num > 1);
 	
 	
 	
 id |      email      
----+-----------------
  1 | hello@gmail.com
  4 | hiii@gmail.com
  6 | yoo@gmail.com

```

==============================================================================================

##Another Soltion
```
DELETE FROM PERSON a USING PERSON b 
	WHERE a.id > b.id AND a.email = b.email AND a.email = 'hello@gmail.com';
	
id |      email      
----+-----------------
  1 | hello@gmail.com
  4 | hiii@gmail.com
  6 | yoo@gmail.com

	
```
