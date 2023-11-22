"""Header
Name:Gabriel
Date:
Version:
Discription:
Algorithm:
1 = ask user for lengths of a, b, h
2 = calculate the area of a trapazoid using the formula and these 3 mesurements (A = (a+b)*h/2)
3 = output the area if the trapazoid to the user
"""

#Discription for user
print("Hello user! This program will ask you for mesurements and calculate the area of a trapazoid using them.")
print("")

#Inputs / mesurements of the trapazoid
a = float(input("What is the top length of the trapazoid?:"))
b = float(input("What is the bottom legnth of the trapazoid?:"))
h = float(input("What is the hight of the trapazoid?:"))

#Calculating the area of the trapazoid
area = (a+b)*h/2

#Outputting the area of the trapazoid to the user'
print("")
print("The total area of a trapazoid with these mesurement is "+str("{0:0.2f}".format(area))+(" units squared"))
