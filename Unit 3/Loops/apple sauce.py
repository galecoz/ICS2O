"""
apple sauce
"""

radius = 0.0
area = 0.0
pie = 3.14
yes = "yes"

while(yes.lower() == "yes"):
    print("")
    radius = float(input("Enter Radius: "))
    area = pie * (radius ** 2)
    print("Area: {0:0.2f} units squared".format(area))
    yes = input("Would you like to run the program again?: ")

print("")
print("toodeloo")

