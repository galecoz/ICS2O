"""Header
name:Gabriel
date:
Version:
Discription:
"""

PIE = 3.14

#Inputs
figureArea = float(input("What is the area of your figure?:"))

#Calc
radius= sqrt(figureArea/PIE)
circumference = radius*2*PIE

sideLength = sqrt(figureArea)

#Output
print("If your figure was a circle, then the raidus would be "+str("{0:.2f}".format(radius)),"and it would have a circumference of "+str("{0:.2f}".format(circumference)))
print("")
print("If your figure was a square instead, then the side length of it would be "+str("{0:.2f}".format(sideLength)))

