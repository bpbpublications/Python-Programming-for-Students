# Parameterized Query in Python Sqlite

import sqlite3
try:
    sqliteConnection = sqlite3.connect(r'C:\sqlite\db\CompanyDatabase.db')
    cursor1 = sqliteConnection.cursor()
    print("Successfully Connected to SQLite Database")
    BookId = input("Enter the book id to update : ")
    price = input("Enter the updated price : ")
    # The question marks ? are placeholders for values.
    # The values of price and Book_Id added to the ? placeholders.
    cursor1.execute("UPDATE BookDetail SET B_price=? WHERE B_id=?", (price, BookId))
    # The rowcount property returns the number of updated rows. Here, 1 row is updated.
    print("Number of rows updated: {}".format(cursor1.rowcount))
    # We select Book id using named placeholder id specified in     dictionary form. Therefore here :id is used as named placeholder.
    cursor1.execute("SELECT * FROM BookDetail WHERE B_id= :id", {"id": BookId})
    row = cursor1.fetchone()   # We retrieve the one selected row
    print(row)
    sqliteConnection.commit()
except sqlite3.Error as error:
    print("Error raised on updating table", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("sqlite connection closed successfully!!")
