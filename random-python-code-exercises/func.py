#NORMAL FUNCTIONS
#def name(firstname):
#   print(f"my name is",firstname)
#name("Prosper")

#MORE THAN ONE ARGUMENT
def names(fname, lname):
    print(f'{lname} comes after {fname}')
names ("prosper", "okoro")

#UNKNOWN ARGUMENT
def names(*name):
    print(f"my name is {name[1]}")
names("prospa", "john", "tee")

#KEYWORD ARGUMENT $ ARBITRARY KEYWORD ARGUMENT
def names(fname="prosper", lname="okoro"):
    print(f"{fname} is my firstname, {lname} is my lastname")
names()

def names(first, last, middle): #3 params, 3 key-values passed when called
    print(f"{first}, then {middle} followed by {last}")
names(first="prosper", last="okoro", middle="tee")

def names(**name): 
    print(f"the fistname is", name["fname"])
names(lname="okoro", fname="pee", mname="tee")

#EMPTY FUNCTION CALL VALUE
def names(name="prosper"): #param has a value
    print(f"my name is {name}")
names() #calling empty function returns value of func param

#LIST AS ARGUMENT
fruits =["apple", "banana", "cherry"]
def food(fruits):
    for x in fruits:
        print(x)
food(fruits)

def foods(beverages):
    for x in beverages:
        print(x)
beverages = ["water", "wine", "beer"]
foods(beverages)

#RETURN VALUES FUNCTION
#def my_num(num):
#    return 5 * num
#num = int(input("enter any number here:"))
#print(my_num(num))

#POSITIONAL_ONLY ARGUMENTS
def num(x,y,/): #argument must be positional when passed
    print(x + y)
num(2,4)

print(" ------")
#KEYWORD_ONLY ARGUMENTS
def num(*, x): #argument must be a keyword when passed
    print(x)
num(x=5)
print(" ------ ")
#COMBINING POSITIONAL AND KEYWORD ARGUMENTS
def num(x,y,/,*,a,b): #when combo positional must come before keyword
    print(a,x,y,b)
num(9,7,a=3,b=5) #order of passing is as order of param above

print(" -------- ")
#RECURSION
def my_recursion(k):
    if k > 0:
        result = (k + 1) + my_recursion(k-1)
        print(result)
    else:
        result = 0
    return result

my_recursion(9)

print("  --------- " )
#LAMBDA FUNCTION, a small ananymous function
def my_lambda(x):
    x = lambda a : 2 * a 
    print(x(3))
my_lambda(3)

#VARAIBLE SCOPE IN FUNCTIONS

score = 0
def my_score(x):
    score += 1
    my_score()
print(score)

print (" ------- ") 
score = 0
def score_me(x):
    global score #using the glocal keyword to incremet score
    score += 1
    print(score)
score_me(1)
print(score)

print(" ------- ")

#OUTER(ENCLOSING) AND INNER(NESTED) FUNCTIONS

def outside():
    x = int(input("enter your value:"))

    def inside():
        nonlocal x
        x += 1
        print(x)
    inside()
    print("modified value of x from inner func is:", x)
outside()
