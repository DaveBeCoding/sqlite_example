# Import module
import sqlite3

# Connecting to sqlite
conn = sqlite3.connect('test.db')

# Creating a cursor object using
# the cursor() method
cursor = conn.cursor()

# Updating
cursor.execute('''DROP TABLE Student;''')

# Commit your changes in the database
conn.commit()

# Closing the connection
conn.close()

# THIS WAS EXAMPLE(S) OF USING C.R.U.D.