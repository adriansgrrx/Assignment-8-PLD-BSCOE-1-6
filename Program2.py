# Program 2: Guess the number
# Generate 1 random number (0-100)
# Ask the user to guess the number
# Display “Greater than” if the inputed number is greater than the random number
# Display “Less than” if the inputed number is less than the random number
# Repeat asking the user until the random number has been guessed correctly.

"""
This program will use randrange module from random library. 
"""
from random import randrange

# generate number from 1-100
randNum = randrange(0,100)
# ask the user for a guess
userGuess = input("Guess a number ranging from 0 to 100: ")

