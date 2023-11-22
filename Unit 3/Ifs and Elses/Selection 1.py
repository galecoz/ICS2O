"""
Selection statements
"""


weight = float(input("Please enter your weight:"))


if weight >0:
    if weight >= 80:
        print("Heavy weight")

    elif weight >=60 and weight <= 79:
        print("Medium weight")

    elif weight <= 59 and weight >0:
        print("Light weight")

if weight <= 0:
    print("invalid weight")
    

