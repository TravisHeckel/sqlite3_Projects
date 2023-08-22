import sqlite3

#I am creating a new database called test.db
conn= sqlite3.connect('test.db')

#This opens that Database and creates an auto increment and a column that is titled file
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_memory( \
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_files TEXT \
                )")
#This commits the changes (applying them) then closes access the database to protect it
    conn.commit()
conn.close()

#This connects to the data base and gives us the list of 'files' the database will have access too.

conn= sqlite3.connect('test.db')

fileList= ('information.docx','Hello.txt','myImage.png', \
           'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

#The with statment checks that Conn = true (or being accessed), sets the control to cursor and
#runs our for loop.
with conn:
    cur = conn.cursor()
    #This for loop will check each item in our fileList, when the if-statement the criteria is met it
    #will place the item on the table in the next available spot.
for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur.execute("INSERT INTO tbl_memory (col_files) VALUES(?)", (x,))
    #This prints out in python letting us know what items where selected. (rather than checking the database everytime.
            print(x)
conn.close()
