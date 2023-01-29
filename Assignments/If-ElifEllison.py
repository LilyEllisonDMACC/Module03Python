"""
Program: If-ElifEllison.py
Author: Lily Ellison
Last date modified: 01/28/2023

The purpose of this program is to ask for the user to sign up for Programmer's Toolkit Monthly Subscription Box and have
them select their level of membership and print out their selection and the cost.
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

"""
Testing:
Input: 1
Expected Output: "You have selected the Free Trial level! There is no cost for this level."
Actual Output: "You have selected the Free Trial level! There is no cost for this level."

Input: 2
Expected Output: "You have selected the Bronze level! Bronze is $10 per month."
Actual Output: "You have selected the Bronze level! Bronze is $10 per month."

Input: 3
Expected Output: "You have selected the Silver level! Silver is $20 per month."
Actual Output: "You have selected the Silver level! Silver is $20 per month."

Input: 4
Expected Output: "You have selected the Gold level! Gold is $30 per month."
Actual Output: "You have selected the Gold level! Gold is $30 per month."

Input: 5
Expected Output: "You have selected the Platinum level! Platinum is $40 per month."
Actual Output: "You have selected the Platinum level! Platinum is $40 per month."

Input: 6
Expected Output: "Invalid entry."
Actual Output: "Invalid entry."

Input: 0
Expected Output: "Invalid entry."
Actual Output: "Invalid entry."

Input: 11
Expected Output: "Invalid entry."
Actual Output: "Invalid entry."

Input: x
Expected Output: "Invalid entry."
Actual Output: "Invalid entry."
"""
