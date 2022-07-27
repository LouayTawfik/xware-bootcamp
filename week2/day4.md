## Exercise 1: Mongodb
#### How connect Mongo Compass to MongoDB
`mongosh'


#### Design Messaging and Notification System in MongoDB
```
use msg_not

db.Messages.insert({sender: {id: 1, name:'Hamada'}, reciever: {id: 1, name:'Hamada2'}, message: {id: 1, name:'Hamada3'}})


db.Messages.insert({sender: {id: 1, name:'Khaled'}, reciever: {id: 1, name:'Mustafa'}, message: {id: 1, name:'hello'}})


db.Notification.insert({sender: {id: 1, name:'Ahmed'}, reciever: {id: 1, name:'Emad'}, type: {id: 1, type:'short'}, content: {id: 1, content:'hey'}, is_read: {id: 1, is_read: 'yes'}, created_at: {id: 1, created_at:'july'}})




```
