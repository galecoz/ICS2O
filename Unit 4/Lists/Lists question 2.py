"""
question 2
"""

import random

fortunes = ["get good","skill issue","2yo timmy better","bot","L"]
restart = "y"

while restart.lower() == "y":
    input("Hit <ENTER> to open your fortune cookie!")
    print(fortunes[random.randrange(5)])

    restart = input("Would you like to restart? [y/n]: ")
    
print("your parental figure")
