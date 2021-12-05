# Program 1: Lottery
# Create a program that ask 3 numbers (0-9) from the user.
# Generate 3 random winning numbers (0-9)
# Display “Winner” if all 3 input numbers matched the generated numbers
# Display ”You loss” if not
# Display ”Try again y/n” after each game
# If the user enter “y” the user will play again
# if “n” the program will exit.
"""
randint will be used from random module in this program including time module
"""
from random import randint
import time

# greetings and briefing
print("\nHi there!")
time.sleep(2)
print("\nWelcome to Lottery House!")
time.sleep(2)
print("\nInstructions:\n1. Enter three(3) numbers of your choice.")
print("2. You can only enter ONE number each and it is your choice if you have your own order. The system won't sort your entries.")
print("3. Keep in mind that you can only enter ONE-POSITIVE-SINGLE-DIGIT-INTEGER, or else the system will not allow your entry!")
print("4. Lastly, enjoy! Best of luck!\n")
time.sleep(3)

# def functionality of the three required random numbers
def get_randWinNum():
    randWinNum1 = randint(0,9)   # randint command from random module to emphasize that the program needs specific integer number
    randWinNum2 = randint(0,9)
    randWinNum3 = randint(0,9)
    return [randWinNum1, randWinNum2, randWinNum3]  # return the variables, [] to indicate list

# def functionality for the 3 inputs from the user.
# while were used on this section 
def get_userNums():
    while True:
        try:
            while True:
                userNum1 = input("Enter your first entry number: ")
                # This line only indictes that the program only accepts numbers from 0 to 9 ONLY.
                if int(userNum1) > 9 or int(userNum1) <= -1:    
                    print("The number must be ranging from 0 to 9.\n")
                else:
                    while True:
                        userNum2 = input("Enter your second entry number: ") 
                        if int(userNum2) > 9 or int(userNum2) <= -1:
                            print("The number must be ranging from 0 to 9.\n")
                        else:    
                            while True:
                                userNum3 = input("Enter your third entry number: ")
                                if int(userNum3) > 9 or int(userNum3) <= -1:
                                    print("The number must be ranging from 0 to 9.\n")
                                else:
                                    return [int(userNum1), int(userNum2), int(userNum3)]    # return the variable, [] to indicate lists
       
        # I used the except functionality for error validation specifically ValueError and EOFError 
        # just to be sure that the program wont exit resuting from any error inputs
        except ValueError or EOFError:
            print("\n[Invalid Input]\nKeep in mind that the Lottery's System only accepts NUMBERS.\nPease try again.\n")

"""
MAIN PROGRAM and FUNCTION CALLING Section
"""
# Global variables
userInterface = "try again"
repeatX = "y"
# Execution and Yes or NO program-user connection section
while userInterface == "try again":
    userNums = get_userNums()
    randWinNums = get_randWinNum()
    userInterface = "_"
    while repeatX == "y":
        repeatX = "_"
        if userNums == randWinNums:
            print(f"\nWinner!\nYou've got the winning numbers! {randWinNums}\nYour Numbers: {userNums}")
        else:
            print(f"\nYou loss.\nThe winning numbers are {randWinNums}\nYour Numbers: {userNums}")
        print("\nDo you wish to try again?\n[y/n]")
    while userInterface == "_":
        repeatX = input("\n>>> ").lower()
        if repeatX == "n":
            print("\nBye! See you next time!\n")
            time.sleep(2)
            userInterface = "exit the program"
        elif repeatX == "y":
            time.sleep(2)
            userInterface = "try again"
# END