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

# Greetings
print("\nWelcome to Guess the Mystery Number!")

# generate a number from 1-100
randNum = randrange(0,100)  #randNum variable = random number
# ask the user for a guess
userGuess = int(input("\nGuess a number ranging from 0 to 100: "))  #userGuess variable = simply the user's guess

# while condition that must satisfy
while userGuess != randNum:
    if userGuess > randNum:
        print("[Incorrect]\nYou need to guess LESS THAN your previous number.")
        userGuess = int(input("\nGuess a number ranging from 0 to 100: "))
    else:
        print("[Incorrect]\nYou need to guess GREATER THAN your previous number.")
        userGuess = int(input("\nGuess a number ranging from 0 to 100: "))
#Display the result after guessing the number correctly
print(f"\nYou successfully guessed the mystery number\nMystery Number: {randNum}\nYour guess: {userGuess}\nCongratulations!\n")
