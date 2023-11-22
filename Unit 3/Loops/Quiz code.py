"""
Name:Gabriel
Date:
Version:
Discription:
"""

#constants
count = 0
totalTemp = 0
avgTemp = 0

#Variables
temperature = float(input("Please enter a temperature less than 100:"))

#Check if its less than 100
while temperature < 100:
    count = count + 1
    totalTemp = totalTemp + temperature
    temperature = float(input("Please enter another temperature:"))

#Calculate the avarage temperature
if count > 0:
    avgTemp = totalTemp / count

#Print the avg temp and the count
print("")
print("-"*30)
print("")
print("You inputed",count,"temperatures with a total avarage temperature of",str("{0:.1f}".format(avgTemp)))
