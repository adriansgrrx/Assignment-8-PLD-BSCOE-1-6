# Program 1: Lottery
# Create a program that ask 3 numbers (0-9) from the user.
# Generate 3 random winning numbers (0-9)
# Display “Winner” if all 3 input numbers matched the generated numbers
# Display ”You loss” if not
# Display ”Try again y/n” after each game
# If the user enter “y” the user will play again
# if “n” the program will exit.

"""
In this program, I will use random module.
"""
import random

def winning_num():
    winningNum = []
    for i in range(3):
        winningN = random.randint(0,9)
        winningNum.append(winningN)
    return winningNum
def user_num():
    userInput = []
    for i in range(3):
        userNums = int(input("Please enter a number: "))
        userInput.append(userNums)
    return userInput

winNum = winning_num()
userNum = user_num()
print(f"Your number is {userNum}\nThe winning number is {winNum}\n")
