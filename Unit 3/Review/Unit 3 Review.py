"""
Write the game of NIM, which is a game where two players remove stones from a pile, one at a
time, until no stones are left. The criteria for the game is as follows:
 Start with a pile of 20 stones
 Each player can only take 1, 2, or 3 stones (never more, never less)
 The player forced to take the last stone loses – in other words, if there is one stone left,
the player must take it
 Display the winner at the end of the game
 Allow the game to be played again (“Would you like to play again? Yes or No: ”)
"""

#Constants and players playing
stones = 20
stonesTaken = 0
restart = "yes"
players = int(input("How many players?: "))
player = 0

print("The pile of stone will start at 20 stones and each person can take from 1-3 stones and the person who takes the last stone loses")


while restart.upper() == "YES": #checks if at the end they inputed yes or no

    while stones > 0: #Makes sure that once there are 0 or less stones it stops

        #Prints how many stones in the pile and sets stones taken to 0 and player to the next player
        print("")
        print("There are",stones,"Stones in the pile")
        stonesTaken = 0
        player = player + 1

        #Varsity loop to demand for 1-3 stones
        while stonesTaken <1 or stonesTaken > 3:
            stonesTaken = int(input("Would you like to take 1,2, or 3 stones Player "+str(player)+str(" ?:")))

        #calculates how many stones in pile after how many were taken
        stones = stones - stonesTaken

        #Checks if the current play is the same as players playing and resets back to 0 so its back at player 1
        if stones > 0 and player == players:
              player = 0

    #Print statements
    print("")
    print("Player",player,"Loses")
    print("")
    restart = input("Would you like to play again? [yes/no] : ")
    print("")

    #asks if they want to play again and if its yes then the loop restarts and anything ends it while also asking for how many stones they want to start with and how many players again for more control 
    if restart.upper() == "YES":
        stones = int(input("How many stone do want to start in the pile for this game?: "))
        player = 0
        players = int(input("How many players?: "))

print("")
print("Thanks for playing")
