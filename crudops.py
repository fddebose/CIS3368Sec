import mysql.connector
import creds


from mysql.connector import Error
from sql import createDB_connection
from sql import execute_query
from sql import execute_read_query


#create connection to mysql database and using the creds.py file with the creds funcion from creds file
myCreds = creds.creds() 
myDbconnection = createDB_connection(myCreds.connectionstring, myCreds.username, myCreds.passwrd, myCreds.dataBaseName)

#CRUD - Create, Read, Update and Delete


#Do we need show each Insert statement for each entry into datab...........?????

#CRUD - Create, Read, Update and Delete
#create a new entry into users table
#query = "insert into sales (seller, product, quantity, price) values ('%s','%s', %d, %d)" % ('Kevin', 'Pen', 20, 3.00)

#uid = 13
#query = "delete from sales where id = %d" % (uid)
#query = "update sales set seller= 'John' where id = %s" % (uid)
#execute_query(myDbconnection, query)

#getting information from database with Select statment 
query = "Select * From sales"
salesdata = execute_read_query(myDbconnection, query)
print(salesdata)

print()

sales_person = []
for i in salesdata:
    if i['seller'] not in sales_person:
        sales_person.append(i['seller'])

print('Available Sellers:\n')
print()

for i in sales_person:
    print(i)

print()

user_input = input("Enter the seller's name:")
print()

user_row = []
for row in salesdata:
    if row['seller'] == user_input:
        user_row.append(row)
print(user_row)

#for i in sales_person:
    #if i == user_input:
        #print('Sales Report for', i,':')

#total = salesdata[0]['quantity'] * salesdata[0]['price']

#print('Product:', salesdata[0]['product'], 'Quantity:', salesdata[0]['quantity'], salesdata[0]['price'], 'Total:', total)
#print('Product:', salesdata[0]['product'], 'Quantity:', salesdata[0]['quantity'], salesdata[0]['price'], 'Total:', total)

'''print('Product:', seller['product'], 'Quantity:', seller['quantity'], seller['price'], 'Total:')

#print('Product:', seller['product'], 'Quantity:', seller['quantity'], seller['price'], 'Total:', total))

#print('Sales Report for', user_input,':')  #need to change print string formatting review......

#seller = user_input   #not sure but I know I ahve to declare variable...........????
for salesman in salesdata:
    if salesman == user_input:
        print(sal)
    else:
        print('OOPs')
       
    print('Sales Report for', seller,':')
    #print(seller)
    total = seller['quantity'] * seller['price']
    print('Product:', seller['product'], 'Quantity:', seller['quantity'], seller['price'], 'Total:', total)


    #print(total) 
    #query = "Select * From sales Where seller= %s" %  (sellers)
    #john_data = execute_read_query(myDbconnection, query)


#print('Product:', seller['product'], 'Quantity:', seller['quantity'], seller['price'], 'Total:') '''


#create a new entry into users table
#query = "Insert into sales (seller, product, quantity, price) values ('%s','%s', %d, %d)" % ('Robert', 'Plate', 10, 10.50)

#execute_query(myDbconnection, query)

'''#additional options with create new data 
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
execute_query(connection, deletetable_query)'''

