
import random

diceWanted = ""
restart = "Yes"
same = ""
roll = 0
yes = "no"

while restart.lower() == "yes":
    
    
    diceWanted = int(input("Would you like to use the 4, 6, 8, 10, 12, or 20 sided dice?: "))
    print("")


    if diceWanted == 4:
        roll = random.randrange(4) +1
        print("You rolled a",roll)

    elif diceWanted == 6:
        roll = random.randrange(6) +1
        print("You rolled a",roll)

    elif diceWanted == 8:
        roll = random.randrange(8) +1
        print("You rolled a",roll)

    elif diceWanted == 10:
        roll = random.randrange(10) +1
        print("You rolled a",roll)

    elif diceWanted == 12:
        roll = random.randrange(12) +1
        print("You rolled a",roll)

    elif diceWanted == 20:
        roll = random.randrange(20) +1
        print("You rolled a",roll)

    restart = input("Would you like to roll again? [yes/no]: ")
    print("-"*30)
    
    
   
                 
print("end")
