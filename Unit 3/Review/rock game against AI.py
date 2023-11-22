"""
kick ass bot in stone game
"""



import random


#Constants and players playing
stones = 20
stonesTaken = 0
restart = "yes"
botStonesTaken = 0
count = 0

print("The pile of stone will start at 20 stones and each person can take from 1-3 stones and the person who takes the last stone loses")


while restart.upper() == "YES": #checks if at the end they inputed yes or no

    while stones > 0: #Makes sure that once there are 0 or less stones it stops

        #Prints how many stones in the pile and sets stones taken to 0 and player to the next player
        print("-"*30)
        print("There are",stones,"Stones in the pile")
        stonesTaken = 0
        print("")


        #Bot takes a random number of stones and now is smart

        if stones -3 == 4:
            botStonesTaken = random.randint(1,2)
        elif stones == 4:
            botStonesTaken = 3
        elif stones == 3:
            botStonesTaken = 2
        elif stones == 2:
            botStonesTaken = 1
        elif stones == 6:
            botStonesTaken = 1
        elif stones == 10:
            botStonesTaken = 1
        elif stones == 8:
            botStonesTaken = 3
        elif stones - 3 == 12:
            botStonesTaken = random.randint(1,2)
        elif stones - 2 == 12:
            botStonesTaken = 1
        else:
            botStonesTaken = random.randint(1,3)
        stones = stones - botStonesTaken



        #Prints bots stones taken and new total
        print("The Bot took",botStonesTaken,"stone")
        count = count + 1
        print("")
        if stones > 0:
            print("There are now",stones,"stones in the pile")
        print("")



        if stones > 0:
            #Varsity loop to demand for 1-3 stones
            while stonesTaken <1 or stonesTaken > 3:
                stonesTaken = int(input("Would you like to take 1,2, or 3 stones Player: "))
            count = count + 1
        

        #calculates how many stones in pile after how many were taken
        stones = stones - stonesTaken

        

    #Print statements that uses the value of the count to find out if the bots or the player won
    print("")
    print("-"*30)
    print("")

    if count%2 == 1:
        print("Player wins")

    else:
        print("Player losses")


    print("")
    restart = input("Would you like to play again? [yes/no] : ")
    print("")

    if restart.upper() == "YES":
        stones = int(input("How many stones would you like to be in this round?: "))
    
    
print("")
print("Thanks for playing")
