"""Header
Name:Gabriel
Date:
Version:
Discription:
"""

import math

#Input
number = int(input("Please enter a 3 diget number:"))

#Calc
hundreds = math.floor(number/100)
tens = math.floor((number - hundreds*100) /10)
ones = math.floor(number - (tens*10) - (hundreds*100))

#Output
print("The hundreds-place digit is:"+str(hundreds))
print("The tens-place digit is:"+str(tens))
print("The ones-place digit is:"+str(ones))

