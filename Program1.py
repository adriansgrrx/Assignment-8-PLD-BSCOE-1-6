import random 
# ----------- CONTEXT ---------------
# Program 1: Lottery
# Create a program that ask 3 numbers (0-9) from the user.
# Generate 3 random winning numbers (0-9)
# Display “Winner” if all 3 input numbers matched the generated numbers
# Display ”You loss” if not
# Display ”Try again y/n” after each game
# If the user enter “y” the user will play again
# if “n” the program will exit.

def get_randWinNum():
    randWinNum1 = random.randint(0,9)
    randWinNum2 = random.randint(0,9)
    randWinNum3 = random.randint(0,9)
    return [randWinNum1, randWinNum2, randWinNum3]

def get_userNums():
    userNum1 = input("\nEnter your first entry number: ")
    userNum2 = input("Enter your second entry number: ") 
    userNum3 = input("Enter your third entry number: ")
    return [int(userNum1), int(userNum2), int(userNum3)]

userInterface = "try again"
repeatX = "y"
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
        repeatX = input("\n> ").lower()
        if repeatX == "n":
            userInterface = "exit the program"
        elif repeatX == "y":
            userInterface = "try again"
        else:
            print("We're sorry. The lottery system can't understand your input.\nDo you wish to try again?[y/n]\n[y] for Yes or [n] for No.\n")