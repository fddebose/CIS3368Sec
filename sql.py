import mysql.connector
from mysql.connector import Error

# Use function to create a connection with the database
def create_connection(hostname, username, passwd, dbname):
    connection = None
    try:
        connection = mysql.connector.connect(
            host= hostname,
            user= username,
            password= passwd,
            database= dbname
        )
        print('connection successful')
    except Error as e:
        print('connection unsuccessful, error is : ', e)
    return connection

#This function is used to execute query to update database (used for insert, update and delete statement)
def execute_query(connectMydB, query):
    mycursor = connectMydB.cursor()
    try:
        mycursor.execute(query)
        connectMydB.commit()
        print('Query successfull')
    except Error as e:
        print('Error occured is: ', e)

# This function is used to execute query to retrive records from database (used for select statements to see results/report)
def execute_read_query(connectMydB, query):
    mycursor = connectMydB.cursor(dictionary = True)
    rows = None
    try:
        mycursor.execute(query)
        rows = mycursor.fetchall()
        return rows
    except Error as e:
        print('Error occured is : ', e)
        