import sqlite3

# connecting to the database
connection = sqlite3.connect("test.db")

# cursor
crsr = connection.cursor()

# execute the command to fetch all the data from the table emp
crsr.execute("SELECT * FROM emp")
  
# store all the fetched data in the ans variable
ans = crsr.fetchall()
  
# Since we have already selected all the data entries
# using the "SELECT *" SQL command and stored them in
# the ans variable, all we need to do now is to print
# out the ans variable
for i in ans:
    print(i)