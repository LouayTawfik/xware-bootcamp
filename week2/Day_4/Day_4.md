## Exercise 1: Mongodb

## Install MongoDB

* Import the public key used by the package management system.

`wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | sudo apt-key add -`

* Create a list file for MongoDB.
`echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list`

* Reload local package database.
`sudo apt-get update`

* Install the MongoDB packages.
`sudo apt-get install -y mongodb-org`

========================================================================

## Install Mongo Compass

https://www.mongodb.com/docs/compass/current/install/


#### How connect Mongo Compass to MongoDB
`mongosh'


#### Design Messaging and Notification System in MongoDB
```
use msg_not

db.Messages.insert({sender: {id: 1, name:'Hamada'}, reciever: {id: 1, name:'Hamada2'}, message: {id: 1, name:'Hamada3'}})


db.Messages.insert({sender: {id: 1, name:'Khaled'}, reciever: {id: 1, name:'Mustafa'}, message: {id: 1, name:'hello'}})


db.Notification.insert({sender: {id: 1, name:'Ahmed'}, reciever: {id: 1, name:'Emad'}, type: {id: 1, type:'short'}, content: {id: 1, content:'hey'}, is_read: {id: 1, is_read: 'yes'}, created_at: {id: 1, created_at:'july'}})




```
