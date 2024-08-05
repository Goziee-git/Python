# a list is a data type in python
# user = ['prospa', 'Dave', 'emma', "bola"]
# print(user)

# # data = [ "me","you"]
# # print(data)
# # emptylsit=[]


# # print("prospa" in emptylsit) #to find if a value exist in the list

# # print(user[-2])
# # print(user[0])

# # print(user.index("prospa")) #to find out the position of a value in the list
# # print(type(user)) #to find the data type

# # print ("")

# # print(user[0:2]) 
# # # print(user[1:-3])
# # # print(user[3:1])

# # # print("")
# # # print(len(user))
# # # user.append("goziee") #to add a value to an existing list
# # # print(user)

# # # ##adding the value to an existing list
# # # print("")
# # # user += ['susu']
# # # print(user)

# # # #using the extend method
# # # print("")
# # # user.extend(['robert','jimmy'])
# # # print(user)

# # # print("")
# # # user.extend(data)
# # # print(user)

#using the insert method
print("")
user.insert(0,"Bob") #to put in a value in a particular index
user[2:2] = ["Eddie", "Alex"]
print(user)

# # # print("")
# # # user[2:3] = ["robert", "JP"]
# # # print(user)

# # # ##removing an item from the list using the remove method
# # # print("")
# # # user.remove("Bob")
# # # print(user)

# # # #removing using the built in function DEl
# # # print("")
# # # del user[0]
# # # print(user)

# # #to remove all the value and return an empty list
# # print("")
# # # user.clear()
# # # print(user)

# # #sorting a list
# # print("")
# # user.sort() ##alphabetical sorting, note lower case comes after uppercase
# # print(user)

# # print("")
# # user.sort(key=str.lower) #we pass the key=str to put the lower case in alphabetical order
# # print(user)

# # nuns = [1 ,20, 40, 15]
# # nuns.reverse() #reverse order
# # print(nuns) 

# # nuns.sort(reverse=True) #highest to lowest, in reverse order
# # print(nuns)

# # print(sorted(nuns, reverse=True)) #using the sorted method globally.

# # nunscopy =  nuns.copy() #to make a copy of the list
# # mynuns = list(nuns)
# # mycopy = nuns[:]

# # print(nuns) 
# # print(nunscopy) 
# # print(mynuns) 
# # print(mycopy) 

# # print("")
# # #we can create a list with a constructor LIST
# # mylist = list(["man", 1, "dan"])
# # print(mylist)


# ##TUPLES
# #the order of the values in the tuples do not change for tuples
# #the syntax of the tuples goes with a parantheses(_)


# mytuple = tuple(('dave', 'man', 34)) ##tuple created with a constructor tuple
# print(type(mytuple))

# print("")
# anothertuple = (1,2,3,4)
# print(anothertuple)
# # (one, *two, hey) = anothertuple
# # print(one)
# # print(hey)
# # print(two)

# print("")
# print(anothertuple.count(1)) 

# print("")
# newlist = list(mytuple)
# newlist.append("neil")
# newtuple = tuple(newlist)
# print(newtuple)
# print(type(newlist))

# print(type(newlist.append("guy"))) ##his is a none type because tuples cannot change in their value


#LIST COMPREHENSION
#allows us to use the fuctionalities of a for-loop
# within a single 

squares = []
for i in range(10):
    squared = i*i
    squares.append(squared)
    print(squares)

#in order to replace this with the list comprehension we do this
print("******************")
squares = [i*i for i in range(10)]
print(squares)
#we can also add conditionals to the list-comprehension
print('   ')
squares = [i*i for i in range(10) if i%2==0]
print(squares)

#this is a form of list comprehension using nested list
print("*************")
def squares():
    numbers = [[2,3,4], [5,6,7], [8,9,0]]
    squared = [[num ** 2 for num in inside_list]for inside_list in numbers]
    print(squared)

squares()
print("   *********   ")
##another example of list comprehension with nested list
students = [["john", 18, "math"], ["mat", 20, "civic"], ["ted", 40, "french"]]
students.pop()
print(students)
print("********")
print(students[1])
print("***********")
student_ages = [[student[1] for student in students]]
print(student_ages)
print("*********")
students.append(["max", 50, "literature"])
print(students)
print("************")
subject = [[subject[2]for subject in students]]
print(subject)
print("***********")

##another example of list comprehension with a matrix(a list of list)
matrix = [[1,2,3], [4,5,6], [7,8,9]]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed)

# this is a form of list comprehension with multiple variable: this allows us to create a new tuple which is combination of several list
numbers = [1,2,3]
letters = ["a","b","c"]
combined = [(num,letter) for num in numbers for letter in letters]
print(combined)

numbers = [1,2,3]
squares = [(num ** 2) for num in numbers]
cubes = [(num ** 3) for num in numbers]
combined = [(num, square, cube) for num in numbers for square in squares for cube in cubes]
#print(combined)
print(">>>>>>>>>")
print(combined[0],combined[13],combined[26])

#using the zip function to combine list items
students = [['john',18,'math'],['mary',12,'english'],['fred',17,'civic']]
name = [student[0] for student in students]
print(name)
age = [student[1] for student in students]
print(age)
course = [student[2] for student in students]
print(course)
combined = [(name, age, course) for name, age, course in zip(name, age, course)]
#the combined list is a new list from all the list
print(">>>>>>")
print(combined)

#to create a list of names or  values from a dictionary
#to get a list from a dictionary
my_dict = {"score1": 1,
        "score2": 2,
        "score3": 3
        }
newlist = list(my_dict.keys()) #to get a list of the keys
print(newlist)
newlist2 = list(my_dict.values()) #to get a list of values
print(newlist2)
newlist3 = list(my_dict.items()) #a list of of both keys and values as a tuple
print(newlist3)
newlist4 = list(newlist3) + (newlist2)
print(newlist4)