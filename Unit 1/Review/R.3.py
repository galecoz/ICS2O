"""Header
Name:GAbriel
Date:
Version:
Discription:
"""

#Varaibles/inputs
PI = 3.14
radius = float(input("What is the radius of a cup in cm?:"))
hight = float(input("What is the hight of a cup in cm?:"))
pitcher = float(input("How much water is curently in the pitcher in cm3?:"))

#Calc
cupVOL = (PI*radius**2)*hight
numCUPS = round(pitcher / cupVOL -.5)

#Output
print(numCUPS,"Cups can be filled with that amount of water")
