"""modules are simply pythin files
the import statement is used for importing classes, functions and specific modules from another module
for example, if we have a module named database.py that conrtains a class that needs to be instantiated from anoter module named products.py, 
there are several syntaxes to achieve this:
|import database
|db = database.Database() #Database is the class, db is the new object, database is the module(name of file)
|
>>this version imports the database module into the product namespace(namespace is the list of names currently accessible in a module or function)
Alternatively we can import just the one class we need from the database.py module
|from database import Database
|db = Database()
|
if the products module already has a class called Database,to avoid confusion, we rename the class when inside the 
products module:
|from database import Database as DB
|db = DB
|
also if we want to import multiple classes/items in one statement
|from database import Database, Query

this technique of importing all the classes, methods from another module using the * wildcard is not good
|from database import * >>this clutters up the namespace and can make code hard to read and maintain
"""
#ORGANIZING MODULES
when our collection grows into more modules, we may need some kind of nested heirachy on our modules. since files cant go into other files but into directories
,these folders(directories) are called packages: a collection of modules in a folder. The name of the package is the name of the folder
to distinguish between a folder (package) from other folders in a directory, we need to place an empty file in folder called (__init__.py)
|Parent_directory/
|  main.py
|  ecommerce/
|     __init__.py
|     database.py
|     products.py
|     payments/
|        __init__.py
|        square.py
|        atripe.py
2 ways to do importation of modules
>>absolute import 
>>relative import 
#ABSOLUTE IMPORTS
"""absolute modules specify the complete path to the module, function,or class we want to import"""
syntaxes
|import ecommerce.products
|product = ecommerce.products.Product()
//OR
|from ecommerce.products import Product
|product = Product()
//OR
|from ecommerce import products
|product = products.Product()
>>"""
these statements use the .dot operator to seperate packages or modules
"""
#RELATIVE IMPORTS
"""Relative imports are basically a way of saying find a class, function, or module as it is positioned realtive to the current module
eg. when Working in the product module and we want to import the Database class from the database module next to it, we could use the relative import
| from .database import Database
in (.database) the period(.) in front of the database says use the database module inside the current package. 
>>if we were editing the paypal  module inside the ecommercee.payment package, we woud want, for example to use the database package inside the parent package instead. This is easily done
with two periods
| from ..database import Database
>>we use more peroids to go further up the heirachy. say for example, if we had an ecoommerce.contact package containing an email module and wanted to import the send_mail function into our paypal module
|from ..contact.email import send_mail
>>importing code directly from packages
for example, we have an ecommerce package containing 2 modules named database.py and product.py


