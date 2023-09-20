import mysql.connector
import creds


from mysql.connector import Error
from sql import create_connection
from sql import execute_query
from sql import execute_read_query

#create connection to mysql database
myCreds = creds.Creds() # getting from creds.py file
connection = create_connection(myCreds.connectionstring, myCreds.username, myCreds.passwd, myCreds.dataBase)

#CRUD - Create, Read, Update and Delete

#create a new entry into users table
query = "insert into users(firstname, lastname, email) values ('test','testlastname','test@uh.edu')"
execute_query(connection, query)

#additional options with create new data 
fname = 'abc'
lname = 'pqr'
myemail = 'xyz@uh.edu'

query = "insert into users(firstname, lastname, email) values ('%s','%s','%s')" % (fname, lname, myemail)
execute_query(connection, query)

#read all users data in users table
query = "select * from users"
users = execute_read_query(connection, query)

for user in users:
    print(user['firstname'], ' ', user['lastname'])

#update a user in user table
uid = 2
query = "update users set email='testlast@uh.edu' where id = %s" % (uid)

execute_query(connection, query)

#delete one user from user table
uid = 2
query = "delete from users where id = %s" % (uid)
execute_query(connection, query)

#additional options with delete
deletetable_query = "drop table users"
execute_query(connection, deletetable_query)

