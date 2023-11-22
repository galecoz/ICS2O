"""Header
Name:Gabriel
Date:
Version:
Discription:
Algorithm: 1=ask user for cost of variables;snacks, Dj, decorations
           2=calculate the number of tickets needed to be sold to have a profit
           3=output expenses and tickets sold needed to user
"""

import math

#Constants
ticketC = 10

#Discription for user
print("Hello, this program will calculate the tickets needed to be sold to gernerate a profit with the expenses inputed at 10$ a ticket")
print("")

#Inputs of costs of the expenses
snacks = float(input("How much was spent on snacks?:"))
Dj = float(input("How much was spent on the Dj?:"))
decor = float(input("How much was spent on decorations?:"))

#Calculate how many tickets are needed to be sold to generate a profit
totalCost = snacks + Dj + decor
ticketsNeeded = math.ceil(totalCost/ticketC)

#Out put total cost and tickets needed to the user
print("")
print("-"*30)
print("")
print("Total Cost:",str("\t\t{0:.2f}".format(totalCost)))
print("Tickets Needed:",str("\t{0:.2f}".format(ticketsNeeded)))
