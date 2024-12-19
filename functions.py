# # # #functions are reuable code
# def hello_world(): #naming functions is done with lowercases and underscores
#     print("Hello world")

# hello_world()

# def sum(num1=3, num2=10):
#     if (type(num1) is not int or type(num2) is not int):
#             return 1
#     return num1 + num2


# total = sum()
# print(total)


# # # #functions that receive unknown number of arguments(*args/params)
# # # def multiple_items(*params):
# # #     print(type(params))
# # #     print(params) 

# # # multiple_items("Dave", "hon", "grace")
 
# # #  #functions that receive a keyword argument (**kwargs/params)

# # # def multiple_named_items(scores):
# # #     scores = [0,1,2,3,4,5,6,7,8,9,10]
# # #     print(type(scores))

     
# # #     for i in scores:
# # #      if (i >= 9):
        
# # #         return sum
# # #      sum = i + 1
    
# # #      print(sum)
# # #     return multiple_named_items(sum)
     
    
    

# # # #how do i call a function with a list
# # # multiple_named_items(scores=[])


# # # def Hello(ArgCount, *VarArgs):
# # #  print("You passed ", ArgCount, " arguments.")
# # #  for i in VarArgs:
# # #     print(i)
# # # Hello(4, "this is a test string")

# # #the RETURN STATEMENT in the function
# # # def DoAdd(Value1, Value2):
# # #  return Value1 + Value2
# # # # print("the sum of 2 and 3 is ", DoAdd(1 + 2))
# # # def DoAdd1(Value1, Value2):
# # #  return Value1 + Value2
# # # print("3 + 4 equals 2 + 5 is ", (DoAdd1(3,4) == DoAdd1(2,5)))

# # # name  = input("tell me your name: ")
# # # print("Hello", name)
# import sys 

# print ("PROSPER DELIGHT MEAL MENU\n")


# print ("1 chocolate")
# print("2 spagfhetti")
# print("3 Beans")

# breakfast = int(input("choose the number that matches your favourite meal \n"))


# if breakfast != ([1,2,3]):
#     tryagain = True
#     while tryagain:
#         def meal_choice(breakfast):

#             if (breakfast == 1):
                
#                 print (" you choose chocolate") 
#                 print("1. vanilla-ice")
#                 print("2. milk")

#                 mix = int(input("enter your choice of chocolate mix: "))
#                 if mix == 1:
#                     print("you choose chocolcate with vanilla-ice")
#                 elif mix == 2:
#                     print("you choose chocolate with milk")
#                 else:
#                     print("we do not serve your favourite mix here")
                
#             if (breakfast == 2):
#                 print("you choose spaghetti")
#                 print("1. meat")
#                 print("2. fish")
#                 meal2 = int(input("enter your choice of mix"))
#                 if meal2 == 1:
#                     print("you choose spaghetti with meat")
#                 elif meal2 == 2:
#                     print("you choose spaghetti with fish")
#                 else:
#                      print("we do not serve your favourite mix here")

#             if (breakfast == 3):
#                 print("you choose Beans")
#                 print("1. bread")
#                 print("2. garri")
#                 combo = int(input("Enter your choice of combo "))
#                 if (combo == 1):
#                     print("you choose Beans with bread")
#                 elif (combo == 2):
#                     print("you choose Beans with garri")
#                 else:
#                     print("we do not have your favourite combo")
            
#     # tryagain = input("\n TryAgain\n y for YES\n Q for Quit \n\n")
#     # if tryagain.lower() == "y":
#     #         continue
#     #     else: 
#     #     print("thanks for trying out here")
#     #     print("see you next time")
#     #     tryagain = False

#         meal_choice(breakfast)
# sys.exit()     

# print("PROSPER'S MEAL MENU\n1. Chocolate\n2. Bread\n")
# breakfast = input("Enter your favourite meal")
# tryagain = True
# while tryagain:
#     def mealmenu(breakfast):


#         if (breakfast == 1):
#             print("you chooose chocolate")
#         else:
#             print("you choose Bread")

def name(first, last):
    first = input("enter your firstname \n")
    last = input("enter your lastname \n")
    fullname = first +" " + last
    print("my fullname is ",fullname)
name("", "")
