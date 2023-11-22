"""Header
Name:Gabriel
Date:October 10th 2023
Version:1
Discription:This program will take the users amount spent on food, clothing, entertainment and rent from last month and output the total amount and the % of each amount
"""

#Inputs
food = float(input("How much did you spend on food last month?:"))
clothing = float(input("How much did you spend on clothing last month?:"))
entertainment = float(input("How much did you spend on entertainment last month?:"))
rent = float(input("How much did you spend on rent last month?:"))

#Calc
totalspent = food + clothing + entertainment + rent
totalfood = food / totalspent * 100
totalclothing = clothing / totalspent * 100
totalentertainment = entertainment / totalspent * 100
totalrent = rent / totalspent * 100

#Output
print("-------------------------------------------")
print("The total amount spent last month was",str("{0:.2f}".format(totalspent))+str("$"))
print("")
print("Category","\tBudget")
print("Food","\t\t"+str("{0:.2f}".format(totalfood))+("%"))
print("Clothing","\t"+str("{0:.2f}".format(totalclothing))+("%"))
print("Entertainment","\t"+str("{0:.2f}".format(totalentertainment))+("%"))
print("Rent","\t\t"+str("{0:.2f}".format(totalrent))+("%"))
    
      
