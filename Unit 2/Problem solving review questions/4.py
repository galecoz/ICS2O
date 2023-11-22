"""Header
Name:Gabriel
Date:
Ver:
Discrip:
-Algorythm-
1=ask user for amount of burgers, fries, and sodas they want
2=calculate the subtotal, tax, and grand total
3=output everything in receipt form
"""

#Constants
BURGERCOST = 4.50
FRIESCOST = 2.50
SODACOST = 1.75
TAX = 0.13


#Varibles/inputs
burgerAmt = int(input("How many bugers would you like?:"))
friesAmt = int(input("How many fries would you like?:"))
sodaAmt = int(input("How many sodas would you like?:"))

#Calculate the sub total, tax, and grand total
subTotal = ((BURGERCOST*burgerAmt)+(FRIESCOST*friesAmt)+(SODACOST*sodaAmt))
tax = subTotal * TAX
total = subTotal + tax

#Output in receipt form to user
print("")
print("-"*30)
print("")
print("SubTotal: \t{0:.2f}".format(subTotal))
print("Tax: \t\t{0:.2f}".format(tax))
print("Total: \t\t{0:.2f}".format(total))
