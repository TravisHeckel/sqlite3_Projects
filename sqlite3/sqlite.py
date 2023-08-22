
#we import the sql module and connect to a database (or create if it doesn't exist)
##import sqlite3
##connection = sqlite3.connect("test_database.db")

#This cursor allows for operations in the database
##c = connection.cursor()

# we create the first  table in the database
##c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")
#we populate the table with our first set of data
##c.execute("INSERT INTO People VALUES('Ron', 'Obvious', 42)")
# we commit the new data to the table and we can IMMEDIATELY SEE THE CHANGE
##connection.commit()

#we are creating a one-time use database. this is normally used for testing code or
#playing around with table structures.
##connection = sqlite3.connect(':memory:')

#This deletes the database IF it exists
##c.execute("DROP TABLE IF EXISTS People")

#We need to close the database connection in order to free up memory and avoid corruption.
##connection.close()


import sqlite3
#doing the connection this way will automatically commit any changes
with sqlite3.connect("test_database.db") as connection:
    #Perform any SQL operations using connection here
    c = connection.cursor()
    c.executescript("""DROP TABLE IF EXISTS People;
                    CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT);
                    INSERT INTO People VALUES('Ron', 'Obvious', 42);
                    """)

peopleValues = (('Luigi', 'Vercotti', 43), ('Arthur', 'Belling', 28))


c.executemany ("INSERT INTO People VALUES (?,?,?)", peopleValues)
