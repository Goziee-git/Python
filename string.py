#string is a data type characterised by alphabets

#literal assignment

first = "prospa" #the word prospa is a string value assigned to the variable first
last = "man" #man is a string value assigned to the variable named last.
 
print(type(first))

print(type(first) == str)
print(type(first) == type(last))
print(isinstance(first, str)) ##using the isinstance command test for datatyoe

# ##constructor function

pizza = str(" ") #value assigned to the variable is constructed to a string using the constrctor function "str"
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str)) #checks the instance of the variable

# joining list items using "join" method
#'join' only works with string iterables
print(' and '.join(['the','man']))
print(" , ".join(['first','last']))
print(">>>>>><<<<<<")

#concatenation of string using
fullname = ["prospa", "john"]
fullname += "enna"
print(fullname)

# #casting a number to a string
decade = str(1980) #3thne number is casted as a string to the variable
print(type(decade))

#putting numbers is a sentence
print("i like rock music from the " + decade + "'s")
#multiple lines
print ("""   Hey how are you today?    
 i am doing well

                            ALl good?
""")

#escaping special characcters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\n\nlocated'
print(sentence)

#methods for formatting cases
name = " bill monroe  "
print(name.title())
print(name.swapcase())
print(name.lower())
print(name.upper())
print(name.strip())
print(name.lstrip())
print(name.rstrip())

#string methods :: methods are functions that are called on a string class

print(first)
print(first.islower())
print(first.isupper())
print(first.isalnum())
print(last.isdigit())
print(last.isdecimal())
print(name.istitle())
print('\n')
print(sentence.title())# title turns all the first letters of each word to upper case.
print(sentence.replace("work", "job"))
print(len(sentence))

#using the string methods to build a food menu

food = "menu".upper() ##we can call a method directly on the value
print(food.center(30, "="))
print("coffee".ljust(16, ".") + "$1".rjust(6))
print("muffin".ljust(16, ".") + "$3".rjust(6))
print("cheesecake".ljust(16, ".") + "$4".rjust(6))
print("Amala".ljust(16, ".") + "$10".rjust(6))

# string index value
names_of_people = ['prospa','stanley','moses']
print(names_of_people[0])
print(names_of_people[2])
print(names_of_people[1])

#some methods return boolean data
print(first.startswith("P")) #startswith method returns a boolean data
print(last.endswith("X")) #endswith method returns a boolean

#casting a string to a number
zipcode = int("10001")
print(type(zipcode))

#methods used to interogate a string
print("willian".startswith("w"))
print("william".startswith("Will"))
print("Prospa".endswith("sPa"))
print("john".isalnum())
print("june12th".isalnum())
print("123".isnumeric())
print("aws".isnumeric())
print("AWS".isupper())
print("aws".islower())
print("Johnny".istitle())
print("johnny".isdecimal())

#String formatting using the "curly braces in string and the FORMAT method"
print("{} comes before {}".format("first","second"))
print("{2} comes befoe {1}, but {0} can also come {1} or even {2}".format("first","second","third"))
#in the line above, the index can also be specified to control the placing of the values into the string

#we can also use names to specify the formats
print("""{name} is the name of my friend, he is {age} years old, {name}
       is very passionate about devOps, 
      he is from {country}"""
      .format(name="prospa",country="nigeria",age="21"))
##here a dictionary is used to supply the name-value format
print(">>>>>>>>>>>")
print(" ")
print(" ")
print("""    """)
values = {"name":"prospa","age":"21"}
print("the boys name is {name}, and he is {age} years old".format(**values))
##here use the list to supply values for the curly braces
list = [1,2,3]
formatted_list = "{0}and {2} and {0} and {1}".format(*list) #numbers refer to list index and *operator to unpax list
print(formatted_list)
#another way to do it using index of list
list = [1,2,3,4]
mylist = "{0[1]} {0[2]} {0[0]} {0[3]}".format(list)
print(mylist)
#its the same syntax when using a list of strings
names = ['prospa',"praise","sani"]
sentence = "{0} is the fist {1} is second {2} is last".format(*names)
print(sentence)
sentence1 = "{0[1]} comes here {0[0]} is here and {0[2]} here".format(names)
print(sentence1)
print(" <><><><><><>   ")
sentence = " and ".join(names)
print(sentence)
print("      ")
#formatting using the f-string: they are prepended before the first quotation mark
#the F-string allows us to embed expressions inside d string literals using curly braces

print("   ")
#f format to embed values of a variable
name = "john"
age = "30"
print("{}is a man,and he is {} old".format(name,age))#usif format.method
message = f'{name}is a man, and he is {age} years old'#usinf the f string to embed a string 
print(message)

word =input('enter something here \n')
here = f'{word} this is what you typed'
print(here)

#performing arithemetic operations
x=5
y=2
result = f"the sum of {x} and {y} is {x + y}"
print(result)
print( "   " )

#use in a function
def greeting(name):
    return f'hello,{name}'
print(greeting("prospa"))
print("  ")
#f used to format the date and time
from datetime import datetime
now = datetime.now()
current_time = f'the current time is {now:%H:%M:%S}'
current_date =f'the current date is {now:%D}'
print(current_time)
print(current_date)
print("  ")
#f for formatting numbers(currency)
price = 19.89
tax = 0.08
total =f'the total is ${price:.4f}' #to four decimal places
print(total)
print("   ")
#f used with dictionaries
dict = {"name":"prospa",
              "age": 30,
              "course": "maths"}
message = f"hello, {dict['name']} you are {dict['age']} and you studied {dict['course']} thank you."
print(message)
print("  ")
#f used with list
fruits = ['berry','grape']
message = f"my favourite fruits are {',' .join(fruits)}"
print(message)
print("  ")
#f used with conditional expressions
is_admin = True
message = f"Welcome, {'admin' if is_admin else 'user'} !"
print(message)
#f used with loops
numbers = [1,2,3,4]
message = f"the numbers are: {[str(num) for num in numbers]} ."
print(message)
print("    ")
#f used with nested f-string
name = "john"
age = 30
message = f"my name is {f'{name}'}. i am {f'{age}'} years old."
print(message)