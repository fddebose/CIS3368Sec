import mysql.connector 
import creds


from mysql.connector import Error
from sql import create_connection
from sql import execute_query
#from sql import execute_read_query



#Create a connection object useing create_connection fuction
myCreds = creds.creds()
connectMydB = create_connection('cis3368class2db.cc6xz6ybkezq.us-east-1.rds.amazonaws.com')

#set object to use cursor fuction to place data in dictionary
mycursor = connectMydB.cursor(dictionary = True)

#create sql object that performs query
query = "Insert into sales(id, seller, product, quantity, price) Values ('John', 'Pencil', 25, 1.50)"
execute_query(connectMydB, query)




