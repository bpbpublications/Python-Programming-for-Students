# Let us consider the following Python application executed in Pycharm IDE that creates a new cursor object and a 
# connection object to connect to a newly created database New_SQLite_Python.db and prints the installed SQLite version details:

import sqlite3    # Import sqlite3 module
try:
    # try keyword encloses a block of code to test for any errors.
    # Create a new connection object
    newConnection = sqlite3.connect(r'C:\sqlite\db\New_SQLite_Python.db')
    cursor = newConnection.cursor()    # Create a new cursor object
    print("New SQLite Database Successfully created and Connected.")
    query1 = "select sqlite_version();"    # New sql query to execute
    cursor.execute(query1)    # Execute query using cursor object
    result = cursor.fetchall()     # Retrieve all rows from result
    print("The current version of SQLite Database is: ", result)
    cursor.close()    # Close the cursor object
except sqlite3.Error as error:
    # except defines a block to handle error raised in try block.
    print("Error while connecting to sqlite", error)
finally:
    # Check if the connection object exists and close the connection
    if newConnection:
        newConnection.close()
        print("Closing the current SQLite connection")
