import sqlite3

# Create a simple SQLite database and a table
sqlite3.connect('Exampledb')


# Connect to the database 
conn = sqlite3.connect('Exampledb')

# create a cursor object which allows us to execute SQL commands
cursor = conn.cursor()

# create a X with raw sql commands
cursor.execute('''INSERT IN YOUR SQL CODE HERE''')

# commit the changes
conn.commit()

# close the connection
conn.close()