"""
this method uses the MySQLdb module which is part of the _mysql module
in reality when a cinnection or operational request is received by (connections.Connection()), 
it is processed and passed to _mysql and sebsequently to the MySQL API in C to perform it.
_mysql uses 2 classes to handle this
>> connection
>> result

connection >> is used to establish connection to the MySQL and thus returns a connection object.
result >> returns a set containing the result from a MySQL command that a program sends. These results can be 
either the query result or an error. _mysql naturally passes the error to the calling process.

to connect to the database
- creating a connection object using the connect() object
- creating a cursor object
- interacting with the database
- closing the connection

"""

import MySQLdb

def connect_to_databasesql():
""" syntax for the connect() object"""
   variable = MySQLdb.connect(
      host="[hostname]",
      user = "[username]", 
      passwd = "[password]",
      db = "[databasename]" )
"""
To connect to the menu database and create a database called menu using the schema in file.sql
use the following steps;
1, mysql -u <user> -p (enter password after the prompt)
2, use the source command to input the schema into the database from within the database
   >> SOURCE /path/to/the/file.sql; file
3, exit the database using \q
"""
"""
after the connection object is created, to interact with the databasae, i create the cursor object
the cursor in MySQL for Python serves as a Python-based proxy for the cursor in a MySQL shell session
the syntax is 
| [cursor name] = [connection object name].cursor()

to interact with db we use
| cursor.execute() 

closing the connection is done in python using the close() method of the db object. for a mydb database, it is done like this

| mydb.close()

closing the db can be done outrightly if the autocommit feature is turned ON, else changes must be committed before closing by calling the commit method of the database object
for the mydb database, it will look like this
| mydb.commit()
we can have multiple db connections also
| mydb1 = MySQLdb.connect
(
 host='host1',
 user='user1',
 passwd='passwd'
 db='db1'                       
)
| mydb2 = MySQLdb.connect
( 
 host='hostname2',
 user='username2',
 passwd='passd'
 db='db'
)
cursor1 = cursor()
cursor2 = cursor()

| these objects cursor1 and cursor1 functions like other variables and object, by calling their methods and atributes separately. 
  we can interact with either of the db and even copy from one to another
|
|
|
 """

cursor = mydb.cursor()