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


=========================================================================================
## Exercise 2_Solution

```
Write an SQL query to report the latest login for all users in the year 2020. Do not include the users who did not login in 2020.
Return the result table in any order.





CREATE TABLE IF NOT EXISTS Login(
	user_id int, time_stamp timestamp, PRIMARY KEY(user_id, time_stamp)
);


INSERT INTO Login(user_id, time_stamp) VALUES(6, '2020-06-30 15:06:07' ),
					       (6, '2020-07-01 14:06:06' ),
					       (6, '2019-03-07 00:18:15' ),
					       (8, '2020-02-01 05:10:53' ),
					       (8, '2020-12-30 00:46:50' ),
			        	       (2, '2020-01-16 02:49:50' ),
					       (2, '2019-08-25 07:59:08' ),
					       (14, '2019-07-14 09:00:00'),
					       (14, '2021-01-06 11:59:59' );
					       
					       
					       
					       
SELECT user_id,
	max(time_stamp)
	AS last_stamp FROM Login
	WHERE time_stamp >= '2020-01-01'
	AND time_stamp < '2021-01-01'
	GROUP BY user_id;
					       
					       
					       
					       
					       

```


## Exercise3_Solution

* Structure of 'restaurants' collection:
```
{
  "address": {
     "building": "1007",
     "coord": [ -73.856077, 40.848447 ],
     "street": "Morris Park Ave",
     "zipcode": "10462"
  },
  "borough": "Bronx",
  "cuisine": "Bakery",
  "grades": [
     { "date": { "$date": 1393804800000 }, "grade": "A", "score": 2 },
     { "date": { "$date": 1378857600000 }, "grade": "A", "score": 6 },
     { "date": { "$date": 1358985600000 }, "grade": "A", "score": 10 },
     { "date": { "$date": 1322006400000 }, "grade": "A", "score": 9 },
     { "date": { "$date": 1299715200000 }, "grade": "B", "score": 14 }
  ],
  "name": "Morris Park Bake Shop",
  "restaurant_id": "30075445"
}
```
* Write a MongoDB query to display all the documents in the collection restaurants.


```
db.restaurants.insert({address: {building :'1907', coord: [-73.856077, 40.848447 ], street: 'Morris Park Ave', zipcode: '10462'}, borough: 'Bronx',cuisine:'Bakery', grades: [ { date: {$date: 1393804800000 }, grade: 'A', score: 2}, { date: {$date: 1378857600000 }, grade: 'A', score: 6 }, { date: { $date: 1358985600000 }, grade: 'A', score: 10}, { date: {$date: 1322006400000 }, grade: 'A', score: 9}, {date: {$date: 1299715200000 }, grade: 'B', score: 14}], name: 'Morris Park Bake Shop', restaurant_id: '30075445'});

```


* Write a MongoDB query to display the fields restaurant_id, name, borough and cuisine for all the documents in the collection restaurant.

```
db.restaurants.find({restaurant_id:"30075445",name:"Morris Park Bake Shop",borough:"Bronx",cuisine:"Bakery"});

```


