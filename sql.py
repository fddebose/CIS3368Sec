import mysql.connector
from mysql.connector import Error
import creds

# Use function to create a connection with the database
def createDB_connection(hostname, username, passwrd, dbname):
    connection = None
    try:
        connection = mysql.connector.connect(
            host= hostname,
            user= username,
            password= passwrd,
            database= dbname
        )
        print('connection successful')
    except Error as e:
        print('connection unsuccessful, error is : ', e)
    return connection


#This function is used to execute query to update database (used for insert, update and delete statement)
def execute_query(myDbconnection, query):
    mycursor = myDbconnection.cursor()
    try:
        mycursor.execute(query)
        myDbconnection.commit()
        print('Query successfull')
    except Error as e:
        print('Error occured is: ', e)
#This fuctiion t exexute read query and places everything in Dictionary 
def execute_read_query(myDbconnection, query):
    mycursor = myDbconnection.cursor(dictionary = True)
    rows = None
    try:
        mycursor.execute(query)
        rows = mycursor.fetchall()
        return rows
    except Error as e:
        print('Error occured is : ', e) 
