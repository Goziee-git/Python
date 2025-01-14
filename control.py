#USING THE WHILE STATEMENT
#value = 0
#while value <=10:
#    print(value)

#while value <=10:
#    value +=1
#    if value == 5:
#        continue #CONTINUE statement skips the rest of the loop when the value is 5
#    else:
#        print("value is now equal to " + str(value))

#names = {"first":"dave", "second":"prospa", "third":"john"}
#using the enumerate function to ouput the index and keys
#for index, key in enumerate(names):
#    print(index, key)
#using the items() method with the enumerate function to ouput the index,key,value
#for index, (key, value), in enumerate(names.items()):
#    print(index, key, value)


    

# import sys

# print("0. red")
# print("1. blue")
# print("2. green")
# print("3. orange")
# print("4. purple")
# print("5. pink")
# print("6. violet")
# print("7. cyan")
# print("8. indigo")
# print("9. black")
# print("10. white")
# user = int(input("enter a value between 1-10 \n "))
# # if user > 10 or user < 0:
# #     sys.exit("you have to enter a number between 1-10")

# # elif user == 0:
# #     print("your colour is RED❤️")
# # elif user == 1:
# #     print("your colour is BLUE💎")
# # elif user == 2:
# #     print("your colour is GREEN💚")
# # elif user == 3:
# #     print("your colour is ORANGE🧡")
# # elif user == 4:
# #     print("your colour is PURPLE💜")
# # elif user == 5:
# #     print("your colour is PINK🩷")
# # elif user == 6:
# #     print("your colour is VIOLET✌🏼")
# # elif user == 7:
# #     print("your colour is CYAN🩵")
# # elif user == 8:
# #     print("your colour is INDIGO🤌🏼")
# # elif user == 9:
# #     print("your colour is BLACK🖤")
# # elif user == 10:
# #     print("your colour is WHITE🤍")
# # else:
# #     print("you entered a wrong number")
    

# print("1. Eggs")
# print("2. Pancakes")
# print("3. Waffles")
# print("4. Oatmeal")
# MainChoice = int(input("Choose a breakfast item: "))
# if (MainChoice == 2):
#  Meal = "Pancakes"
# elif (MainChoice == 3):
#  Meal = "Waffles"
# if (MainChoice == 1):
#  print("1. Wheat Toast")
#  print("2. Sour Dough")
#  print("3. Rye Toast")
#  print("4. Pancakes")
#  Bread = int(input("Choose a type of bread: "))
#  if (Bread == 1):
#     print("You chose eggs with wheat toast.")
#  elif (Bread == 2):
#     print("You chose eggs with sour dough.")
#  elif (Bread == 3):
#     print("You chose eggs with rye toast.")
#  elif (Bread == 4):
#     print("You chose eggs with pancakes.")
#  else:
#     print("We have eggs, but not that kind of bread.")
 
# elif (MainChoice == 2) or (MainChoice == 3):
#  print("1. Syrup")
#  print("2. Strawberries")
#  print("3. Powdered Sugar")
#  Topping = int(input("Choose a topping: "))
#  if (Topping == 1):
#     print ("You chose " + Meal + " with syrup.")
#  elif (Topping == 2):
#     print ("You chose " + Meal + " with strawberries.")
#  elif (Topping == 3):
#     print ("You chose " + Meal + " with powdered sugar.")
#  else:
#     print ("We have " + Meal + ", but not that topping.")
 
# elif (MainChoice == 4):
#  print("You chose oatmeal.")
 
# else:
#  print("We don't serve that breakfast item!")


# ##NESTED LOOOPS
# names = ["propsa", "johnpaul", "gabriel"]
# actions = ["eats", "codes", "sleep"]
# responses = ["well", "expertly", "soundly"]
# for name in names:
#  for action in actions:
#         for response in responses:
#           print(name + " " + action + " " + response + ".")

# print(" ")

# names = ["propsa", "johnpaul", "gabriel"]
# actions = ["eats", "codes", "sleep"]
# for action in actions:
#  for name in names:
#         print(name + " " + action + ".")


# for name in ["prospa","rejoice","praise"]:
#     print("the name is ",name)

# people = ["john","guy","bittle"]
# for i in people:
#     print(i)


# LetterNum = 1
# for Letter in "Howdy!":
#  print("Letter ", LetterNum, " is ", Letter)
#  LetterNum+=1

# numletter = 1

# for i in "prospa":
#  print("letter ", numletter, " is ", i)
#  numletter+=1


###USING THE BREAK STATEMENT 
# string = input("enter any length of string \n")
# if (len(string) >= 10):
#     print("you entered a string with more than 10 letters")
#     print("the length of the string is ",len(string))
# else:
#     str_length = 1
# for letter in string:
#     print("the letter ",letter,"is", str_length)
#     str_length += 1
#     if str_length == 8:
#         print("the program breaks at the eight alphabet")
#         break




# letter = "PROSPA"
# str_num = 1
# for i in letter:
  
#     if i == "S":
#         continue
#         print("we encountered an S")
#     print("the letter ", str_num," is", i)
#     str_num += 1


# letter = "PROSPA"
# str_num = 1
# for i in letter:
  
#     if i == "S":
#         pass
#         print("we encountered an S")
#     print("the letter ", str_num," is", i)
#     str_num += 1


#using the pass statement


# letter = "persistence"
# str_num = 1
# for i in letter:
#     if (i != "s"):
#         pass
#         print("the letter ",str_num, " is", i)
#         str_num += 1
#     elif i == "s":
#         print("the letter here is ", i )
#         str_num += 1

#using the FOR-ELSE Statement
# Value = input("Type less than 6 characters: ")
# LetterNum = 1
# for Letter in Value:
#  print("Letter ", LetterNum, " is ", Letter)
#  LetterNum+=1
# else:
#  print("The string is blank.")

#using a simple WHILE STATEMENT 
# three task that must be performed when using a while loop are
# 1: set the environment for the comdition: sum = 0
# 2: put the condition within the loop for the execution of the loop
# 3: set a limit for the codition to be met and the loop to be terminated
# it is needed to prevent the endless execution of a while Loop   
# Sum = 0
# while Sum < 5:
#  print(Sum)
#  Sum+=1


##ERROR HANDLING
# try:
#  Value = int(input("Type a number between 1 and 10: "))
# except ValueError:
#  print("You must type a number between 1 and 10!")
# else:
#  if (Value > 0) and (Value <= 10):
#     print("You typed: ", Value)
#  else:
#     print("The value you typed is incorrect!")


# try:
#     Value = int(input("Type a number between 1 and 10: "))
# except (ValueError, KeyboardInterrupt):
#   print("You must type a number between 1 and 10!")
# else:
#   if (Value > 0) and (Value <= 10):
#     print("You typed: ", Value)
#   else:
#    print("The value you typed is incorrect!")


..................................

# def calculate_average():
#     total = 0
#     count = 0
#     while True :
#         try:
#             num = input("Enter a number (or 'q' to quit): ")
#             if num.lower() == 'q':
#                 break
#             num = float(num)
#             total += num
#             count += 1
#         except ValueError:
#             print("Invalid input! Please enter a number. ")
#             if count > 0:
#                 average = total / count
#                 return average
#             else:
#                 return "no numbers entered!"
            
# print(calculate_average())  

#tryagain = True
#while tryagain:
#   user = input("do u want to try again, Y for YES, or q for QUIT")
#    if user == "y":
#       print("playagain")
#   else:
#        try:
#            if user == "q":
#                pass
#        except:
#            print("an error occurerd")
#        break

#USING THE MATCH-CASE STATEMENT
data_type = input("any input:" )

match data_type:
    case str() | int() | float():
        if case == str():
            print ("you enter a string:")
        elif case == int():
            print("you entered an integer:")
        elif case == float():
            print("you entered a float value")
    case _:
        print("you entered something else")