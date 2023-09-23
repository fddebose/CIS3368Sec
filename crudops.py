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

sales_person = []
for i in salesdata:
    if i['seller'] not in sales_person:
        sales_person.append(i['seller'])

print('Available Sellers:\n')


for i in sales_person:
    print(i)
    print()

print()

user_input = input("Enter the seller's name: ")
print()

user_row = []
for row in salesdata:
    if row['seller'] == user_input:
        user_row.append(row)

#for row in range(len(user_row)):
    #print(user_row[row])

print()
print(f"Sales Report for {user_input}:")
print()

total=0
total2 =0
for row in user_row:
    total = row['quantity'] * row['price']
    total2 += total 
    print(f"Product: {row['product']}, Quantity: {row['quantity']}, Price: {row['price']}, Total: {total}")
    print()

print(f"Total Sales for {user_input}: ${total2}")  

