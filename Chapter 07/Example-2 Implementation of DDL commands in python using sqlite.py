# Let us see the implementation of DDL commands in Python using SQLite3 module

import sqlite3
try:
    sqliteConnection = sqlite3.connect(r'C:\sqlite\db\CompanyDatabase.db')
    query1 = '''CREATE TABLE Staff ( s_id INTEGER , s_name TEXT, s_email text, s_joining_date TEXT, s_salary REAL);'''
    cursor1 = sqliteConnection.cursor()
    print("Successfully Connected to SQLite Database")
    cursor1.execute(query1)
    sqliteConnection.commit()
    print("SQLite table created successfully")
    cursor1.close()
    cursor2 = sqliteConnection.cursor()
    query2 = '''ALTER TABLE Staff ADD s_age INTEGER'''
    cursor2.execute(query2)
    sqliteConnection.commit()
    print("SQLite table altered successfully")
    cursor2.close()
except sqlite3.Error as error:
    print("Error raised on creating table", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("sqlite connection closed successfully!!")
