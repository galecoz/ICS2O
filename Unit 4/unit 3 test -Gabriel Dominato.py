"""Header
Name:Gabriel
Date:6 nov 2023
Ver:1
Discription:Unit 3 or idk test
"""

import time, random

#Constants / all the different values set to each player to allow the program to function
dice = 6
p1roll = 0
p2roll = 0
p1rollF = 5
p2rollF = 5
p1count = 0
p2count = 0
replay = "yes"

#Names of players
p1name = input("Who is the first player?: ")
p2name = input("Who is the second player?: ")

#A restart loop to allow the program to be replayed without restarting it entirely
while replay.lower() == "yes":

    #Does the rolls for player 1 by checking to see if the dice rolls are greater than 4
    while p1rollF > 4:

        p1rollF = 0                         #Resets the combined total roll to 0


        #Does the 2 rolls and adds them to the total of the 2
        p1roll = random.randrange(dice) + 1
        p1rollF = p1rollF + p1roll
        p1roll = random.randrange(dice) + 1
        p1rollF = p1rollF + p1roll

        p1count = p1count + 1               #Tells you how many rolls of both dice it took to get below or equal to 4
    
    #Does the same rolls for player 2
    while p2rollF > 4:
        p2rollF = 0                        

        p2roll = random.randrange(dice) + 1
        p2rollF = p2rollF + p2roll
        p2roll = random.randrange(dice) + 1
        p2rollF = p2rollF + p2roll

        p2count = p2count + 1               


    #Prints the players names and their total rolls 
    print("-"*30)
    print("Player"," \t# of Rolls")
    print(p1name,"\t\t",p1count)
    print(p2name,"\t\t",p2count)
    print("")

    #A set of if and elses to check who won and print it
    if p1count < p2count:
        print(p1name,"Wins!")

    else:
        print(p2name,"Wins!")

    #Asks the user if they would like to reroll and play again and if they do it resets all the variables back to their base values
    replay = input("Would you like to reroll? [yes/no]: ")
    if replay.lower() == "yes":
        replay = "yes"
        p1roll = 0
        p2roll = 0
        p1rollF = 5
        p2rollF = 5
        p1count = 0
        p2count = 0
        
    else:
        replay = "no"


#Final goodbye
print("")
print("Thanks for playing")




















