# Program 1: Lottery
# Create a program that ask 3 numbers (0-9) from the user.
# Generate 3 random winning numbers (0-9)
# Display “Winner” if all 3 input numbers matched the generated numbers
# Display ”You loss” if not
# Display ”Try again y/n” after each game
# If the user enter “y” the user will play again
# if “n” the program will exit.

"""
In this program, I will use random module and time module.
"""
import random
import time

winningNum = [] # A variable with an empty list designated to store the 3 required random numbers

for i in range(0,3): # for loop to assign a maximum of three(3) numbers
    randNum = random.randint(0, 9)  # a special variable whose to generate random integers ranging from 0-9 
    
    # while functionality to generate unique numbers
    while randNum in winningNum:
        randNum = random.randint(0, 9)
    # after generating unique random numbers it will now be stored/add to the empty list using the ".append" command. 
    winningNum.append(randNum)
winningNum.sort() # Sort the generated winning numbers ascending to look more organized.and.
# Display the winning numbers.
print(f"The winning numbers are {winningNum}")