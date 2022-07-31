##Exersice1_Solution

```
CREATE TABLE IF NOT EXISTS PERSON(
	id serial PRIMARY KEY,
	email varchar(40) CHECK(LOWER(email) = email)
);


IINSERT INTO PERSON(email) VALUES('john@example.com'), ('john@example.com'), ('bob@example.com'),
		('john@example.com'), ('john@example.com'), ('john@example.com');
		
		
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




DELETE FROM PERSON a USING PERSON b 
	WHERE a.id > b.id AND a.email = b.email;
	
 id |      email       
----+------------------
  1 | john@example.com
  3 | bob@example.com



```


