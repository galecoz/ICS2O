"""Header
Name:Gabriel
Date:
Version:
Discription:
"""

import math

#Variables
GALLONCOST = 29.99

#Discription for user
print("This program will calculate the total surface area of all 4 of the walls in a room")
print("Please mesure and input these amounts as feet")
print("")

#Input
print("----------------------------------")
w1 = float(input("Enter the width of the first wall:"))
w2 = float(input("Enter the width of the second wall:"))
h1 = float(input("Enter the hight of a wall:"))
print("----------------------------------")
print("")
print("")
print("----------------------------------")

#Calc
sA1 = w1 * h1
sA2 = w2 * h1

TsA = (sA1 + sA2) * 2
gallonsRQ = math.ceil(TsA / 300)
gallonsC = GALLONCOST * gallonsRQ

#Output
print("The surface area of the first wall in sqare feet is:" + str("{0:.1f}".format(sA1)))
print("The surface area of the second wall in sqare feet is:" + str("{0:.1f}".format(sA2)))
print("The total combined surface area of the four walls in sqare feet is:" + str("{0:.1f}".format(TsA)))
print("----------------------------------")
print("To paint these walls",gallonsRQ,"gallons of paint costing",str(GALLONCOST)+ str("$"),"per gallon for a total cost of " +str("{0:.2f}".format(gallonsC)) + str("$"),"to paint all 4 walls")
