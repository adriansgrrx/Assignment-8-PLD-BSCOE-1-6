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
import time

# Greetings
print("\nWelcome to Guess the Mystery Number!")
time.sleep(2)
print("\nInstructions:\n1. In this program, the user is required to enter his/her guess.\n2. The user have unlimited guess until getting into the mystery number.\n3. The system don't process inputs that is negative. The number should only range from 0 to 100.\n4. The system will give hints for every incorrect guess like [Greater than] and [Less than].\n5. Lastly, enjoy and have fun!")
time.sleep(2)

# generate a number from 0-100
randNum = randrange(0,100)  #randNum variable = random number

# while condition that must satisfy
while randNum != "user guess":
    try:
        # ask the user for a guess
        userGuess = int(input("\nGuess a number ranging from 0 to 100: "))  #userGuess variable = simply the user's guess
        if int(userGuess) != int(randNum):  # condition if the user guess didn't match the random number
            if int(userGuess) > int(randNum): # if need higher number
                print("[Incorrect]\nHINT: Greater than")
            elif int(userGuess) < int(randNum): # if need lower number
                print("[Incorrect]\nHINT: Less than")
        elif int(userGuess) == int(randNum): # condition if the user guess matched the random number
            randNum = "user guess"
        if int(userGuess) > 100:
            print("Please try again. Keep in mind that the system range is from 0 to 100 ONLY.")
            continue;
        elif int(userGuess) < 0:
            print("Please try again. Keep in mind that the system range is from 0 to 100 ONLY.")
            continue;   
    # I used the except functionality for error validation specifically ValueError and EOFError 
    # just to be sure that the program wont exit resuting from any error inputs
    except ValueError or EOFError:
        print("[Invalid Input]\nThe system only accept INTEGERS. Please do not include any other characters.\nPlease try again.")
else:
    #Display the result after guessing the number correctly
    print(f"\nCongratulations!\nYou successfully guessed the mystery number!\nMystery Number: {userGuess}\n")