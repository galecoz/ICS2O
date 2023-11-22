"""Header
Name:Gabriel
Date:
Version:
Discription:
"""

#Variables
balance = 400
print("Current balance:",balance)
print("--------------------")
withdraw = float(input("How much would you like to withdraw?:"))
deposit = float(input("How much would you like to deposit?:"))

#Calc
newbal = balance - withdraw + deposit


#Output
print("--------------------")
print("New balance:"+str("{0:.2f}".format(newbal)))
