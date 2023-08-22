##import sqlite3

#get personal data from user
##firstName = input("Enter your first name: ")
##lastName = input("Enter your last name: ")
##age = int(input("enter your age: "))
##personData = (firstName, lastName, age)

#execute insert statement for supplied person data
## with sqlite3.connect('test_database.db') as connection:
##    c = connection.cursor()
##    line = "INSERT INTO People VALUES ('"+ firstName +"', '"+ lastName +"', " + str(age) +")"
##    c.execute(line)
##    print(line)
##    c.execute("INSERT INTO People VALUES(?,?,?)", personData)

##    c.execute("UPDATE People SET Age=? WHERE FirstName=? AND LastName = ?",(43, 'Luigi', 'Vercotti'))

##    c.execute("DROP TABLE IF EXISTS People")

import sqlite3

peopleValues = (('Ron', 'Obvious', 42), ('Luigi', 'Vercotti', 43), ('Arthur', 'Belling', 28))

with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS People")
    c.execute("CREATE TABLE People (FirstName TEXT, LastName TEXT, Age INT) ")
    c.executemany("INSERT INTO People VALUES (?, ?, ?)",
                  peopleValues)

#select all first and last name from people over the age of 30
    c.execute("SELECT FirstName, LastName FROM People WHERE Age > 30")
    while True:
        row = c.fetchone()
        if row is None:
            break
        print(row)
