"""
Program: If-ElifEllison.py
Author: Lily Ellison
Last date modified: 01/28/2023

The purpose of this program is to ask for the user to sign up for Programmer's Toolkit Monthly Subscription Box and have
them select their level of membership and print out their selection and the cost.

"""


"""
Each month is something different, t-shirts, stickers, figurines, even programming books!
The levels are the following:

    Platinum
    Gold
    Silver
    Bronze
    Free Trial

Platinum is $60, each level below is 10 dollars cheaper, and the free trial is free. Write a program that uses a
selection statement, getting user's input for a level and printing the cost for that level.
Submit your .py file.
As an example, after it describes the Subscription box levels, it then says "which level would you like to try?" if I
enter "silver" or something equating to level silver - it should say something like "Silver is $40 a month. Thanks for
selecting that"
"""

#setting constant variables to do calculations to make print commands easier to adjust to the levels
BASE_FEE = 10 #pricing starts at $10
ADJUST = 1 #since the first selection is free and I started numbering at 1, I had to subtract 1 from the selection to
            #make for easier calculations

#display of initial information:
print("Thank you for your interest in our Programmer's Toolkit Monthly Subscription Box!")
print("Please enter the number of your desired subscription level from the list below:")
print("1. \"Free Trial\" level: access to our forums, email updates, and get an enamel pin.")
print("2. \"Bronze\" level: everything from the lower level and monthly stickers.")
print("3. \"Silver\" level: everything from the lower levels and a figurine every 2 months.")
print("4. \"Gold\" level: everything from the lower levels and a T-shirt every quarter.")
print("5. \"Platinum\" level: everything from the lower levels and our annual programming book of the year.")

#Collects and displays user's input
userInput = input("Your selection: ")
#Checks if user's input is valid
if(userInput == '1' or userInput == '2' or userInput == '3' or userInput == '4' or userInput == '5'):
    levelSelectInt = int(userInput)#casts input from string to integer for easier calculations
    levelFee = (levelSelectInt - ADJUST) * BASE_FEE #calculates fee for the level

    if(levelSelectInt == 1): #if statement for first option
        levelName = "Free Trial" #setting the level name as a variable helps make the code more universal I think
        print("You have selected the " + levelName + " level! There is no cost for this level.")

    elif(levelSelectInt == 2): #first of four elif statements to select levels
        levelName = "Bronze"
        print("You have selected the " + levelName + " level! " + levelName + " is $" + str(levelFee) + " per month.")

    elif (levelSelectInt == 3):
        levelName = "Silver"
        print("You have selected the " + levelName + " level! " + levelName + " is $" + str(levelFee) + " per month.")

    elif (levelSelectInt == 4):
        levelName = "Gold"
        print("You have selected the " + levelName + " level! " + levelName + " is $" + str(levelFee) + " per month.")

    elif (levelSelectInt == 5):
        levelName = "Platinum"
        print("You have selected the " + levelName + " level! " + levelName + " is $" + str(levelFee) + " per month.")
        #"if" branch rejoins main after this

else: #else statement selects all numbers outside the 1 - 5 range and all non-number entries
    print("Invalid entry.")
