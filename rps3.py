import sys
import random
from enum import Enum

class RPS(Enum): #to make the values fixed globally in the program

   ROCK = 1
   PAPER = 2
   SCISSORS = 3

playagain = True

while playagain:


    print("")
    playerchoice = input("Enter ... \n1 for Rock, \n2 for Paper, or \n3 for scissors \n")

    player = int(playerchoice) ##we do this because all the user inputs must be an interger

    if player < 1 or player > 3: #the | symbol is read as OR
    #this is a codeblock, to prevent the program from doing anything other than what we want it to do
    #note here that when it runs here without the "sys module" control woudlnt be retruned to the user

        sys.exit("you must enter 1, 2,or 3") #returns control to the user 

    computerchoice= random.choice("123") #this allows the computer to make a random choice.
    computer = int(computerchoice)

    print("")
    print("you chose " + str(RPS(player)).replace("RPS.", " ") + ".")
    print("python chose " + str(RPS(computer)).replace("RPS.", " ") + ".")
    print("")

    #we use a control statement to implement the logic of the game

    if player == 1 and computer == 3:
        print("🎉player wins")
    elif player == 2 and computer == 1:
        print("🎉player wins")
    elif player == 3 and computer == 2:
        print("🎉player wins")
    elif player == computer:
        print("👌tie game")   
    else:
        print("😍python wins")

    playagain = input("\nplay again? \nY for yes or \nQ for Quit \n\n")
    if playagain.lower() == "y":
     continue
    else:
       print("🎉🎉🎉🎉🎉")
       print("thank you for playing")
       playagain = False
sys.exit("bye❤️")