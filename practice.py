from list import squares


def add_one(num):
    if (num >=9):
        return num + 1
    total = num + 1
    print(total)

    return add_one(total) #this is a recursive call within a function
    
newtotal = add_one(0)
print(newtotal)

#using the curly braces with the format method
print( "{0} {2} {1} {3} ".format("prospa","john","prince","promise"))
print( """ in {country}, there was a man named {name}, and he was {age} years old """.format(name="prospa",country="mali",age=21))
list = ["man", 30, True]
print("the {} about{} feets tall is not {}".format(*list))
dict = {
    "name":"prospa",
    "age": 20,
    "nationality":"Nigerian"
}

print("{3},{0},{2},{1}".format("pro","man","boy","girl"))
print( """there was a man named {name}, in is early {score}, he scored {age} """.format(name="prosper",age="21",score="30"))



# print( """i am from {origin} my name is {name} i am {age} years old""".format(name=input("name here:"),age=input("how old:"),origin=input("where from:")))

#QUESTION: how to unpack a tuple and dict using the * operator with the format method
list = []
for i in range(5):
    square = i * i
    list.append(square)
    print(list)
    continue

#doing the same above using the list comprehension:
print("><><><><><<><")
list = [i * i for i in range(5)]
print(list)

#to print a single  list with all the numbers in list
 
newlist = [[list[0], list[1], list[2], list[3]] for innerlist in list]
print(newlist)

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





