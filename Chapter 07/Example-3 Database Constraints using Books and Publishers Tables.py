# Let us see an example of creating BookDetail and PublisherDetail tables and applying various table constraints to them:

import sqlite3
try:
    sqliteConnection = sqlite3.connect(r'C:\sqlite\db\CompanyDatabase.db')
    cursor1 = sqliteConnection.cursor()
    print("Successfully Connected to SQLite Database")
    # executescript method allows executing whole SQL code in 1 step
    cursor1.executescript("""      
        DROP TABLE IF EXISTS PublisherDetail;  #Drop table if exists
        CREATE TABLE PublisherDetail (P_id INTEGER PRIMARY KEY, 
        P_name TEXT NOT NULL);
        INSERT INTO PublisherDetail VALUES(101,'BPB Publication');
        INSERT INTO PublisherDetail VALUES(102,'Wiley Publication');
        INSERT INTO PublisherDetail VALUES(103,'McGraw Hill');
        INSERT INTO PublisherDetail VALUES(104,'CRC Press');
        DROP TABLE IF EXISTS BookDetail;
        CREATE TABLE BookDetail (B_id INTEGER PRIMARY KEY, B_name TEXT NOT NULL, B_type TEXT NOT NULL, B_price REAL, pid INTEGER,
        FOREIGN KEY (pid) REFERENCES PublisherDetail);
        INSERT INTO BookDetail VALUES(9001,'Learn Python', 'Programming', 500, 101);
        INSERT INTO BookDetail VALUES(9002,'Operating Systems', 'Programming', 700, 102);
        INSERT INTO BookDetail VALUES(9003,'Learn C++', 'Programming', 400, 101);
        INSERT INTO BookDetail VALUES(9004,'Europe and the East', 'Literature', 1000, 104);
        INSERT INTO BookDetail VALUES(9005,'The Book Thief', 'Fiction', 1500, NULL);
        """)
    print("SQLite tables created successfully!!")
    print("The details of Books are:")
    cursor1.execute("SELECT * FROM BookDetail")
    rows = cursor1.fetchall()
    for r1 in rows:
        print(r1)
    print("The details of Publishers are:")
    cursor1.execute("SELECT * FROM PublisherDetail")
    rows = cursor1.fetchall()
    for r2 in rows:
        print(r2)
    sqliteConnection.commit()   # All changes must be committed 
except sqlite3.Error as error:
    # In case of an error, the changes are rolled back and an error message is printed to the terminal.
    print("Error raised on executing 1 or more commands", error)
    if sqliteConnection:
        sqliteConnection.rollback()
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("sqlite connection closed successfully!!")
