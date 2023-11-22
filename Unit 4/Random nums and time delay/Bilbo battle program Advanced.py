bilboLVL = 1
goblinLVL = 1
hpLVLmultiplyerBilbo = .1
hpLVLmultiplyerGoblin = .2
BonusHP = 0

bilboHP = 100
goblinHP = 75

bilboATK = 0
goblinATK = 0
bilboCC = 0
goblinCC = 0
bonusDMG = 0
click_count = 0
goblinBASErange = 10
goblinMAXrange = 15


gamerun = "yes"
restart = "yes"
hit  = 0
hits = 0
lvlPrint = "yes"
inp = "yes"

startTime = 0
currentTime = 0

import random, time

#Do weapons and armor before more goblins/higher dif
#-------------------------------------------------------------------------------------

#Allows game to be replayed if bilbo is defeated
while restart.lower() == "yes" :

    #Allows for multiple levels
    while gamerun.lower() == "yes":


        #Checks if their lvls are above 1 so it doesnt multiply by 0 and calculates bonus hp then adds that to their base hp
        if bilboLVL != 1:
            bonusHP = bilboHP * (hpLVLmultiplyerBilbo * (bilboLVL - 1))
            bilboHP = bilboHP + bonusHP

        if goblinLVL != 1:
            bonusHP = goblinHP * (hpLVLmultiplyerGoblin * (goblinLVL - 1))
            goblinHP = goblinHP + bonusHP
            goblinBASErange = goblinBASErange + 5
            goblinMAXrange = goblinMAXrange + 5

 
        #The game
        while bilboHP > 0 and goblinHP > 0:
            if lvlPrint == "yes":
                print("Level",bilboLVL)
                print("-"*30)

           
            
            #HP statements
            print("LVL",goblinLVL,"Goblin HP: ",str("{0:0.1f}".format(goblinHP)))
            print("LVL",bilboLVL,"Bilbo HP: ",str("{0:0.1f}".format(bilboHP)))
            print("")
            time.sleep(1)

            #Calculates crit chance
            bilboCC = random.randint(1,3)
            goblinCC = random.randint(1,6)


            #decides between if its a crit or not and calculates and deals dmg
            if goblinCC == 1:                                            #goblin
                goblinATK = random.randint(goblinBASErange,goblinMAXrange) *  2
                print("The goblin hit a CRITICAL  and dealt",goblinATK,"damage to bilbo")

            else:                                                       #goblin
                goblinATK = random.randint(goblinBASErange,goblinMAXrange)
                print("The goblin dealt",goblinATK,"damage to bilbo")
            print("")

            bilboHP = bilboHP - goblinATK
            time.sleep(1)

            #use an input calculator and let the player spam to increase their dmg range
            click_count = 0
            print("To increase bilbo's atk range, Spam enter for 3secs! [delete any extra enters after time is done]")

            #Takes the real current time and resets the hits to 0
            currentTime = 0
            
            hits = 0
           
            hit = input("Spam!")
            startTime = round(time.time())


            #Uses the start time and checks if the current time is not equal to start time +3 alowing 3 secs of spam
            while currentTime != round(startTime + 3) and currentTime < round(startTime + 3):

                currentTime = round(time.time())
                hit = input("spam!")
                if hit == "":
                    hits = hits + 1
            
            #Bonus dmg calculator
            
            bonusDMG = 0
            bonusDMG = .5 * hits

            #calculates biblos dmg
            if bilboCC == 1:                                             #bilbo
                bilboATK = (random.randint(5,15)+ bonusDMG)*  2 
                print("Bilbo hit a CRITICAL  and dealt",str("{0:0.1f}".format(bilboATK)),"damage to the goblin")

            else:                                                        #bilbo
                bilboATK = (random.randint(5,15) + bonusDMG)
                print("Bilbo dealt",str("{0:0.1f}".format(bilboATK)),"damage to the goblin")
            print("-"*30)

            goblinHP = goblinHP - bilboATK
            time.sleep(4)

        #Makes it so the print that says which lvl only shows at the start of each lvl
            lvlPrint = "no"
        lvlPrint = "yes"
        
        #tells if biblo or the goblin 
        if bilboHP > 0:
            bilboLVL = bilboLVL + 1
            goblinLVL = goblinLVL + 1
            print("Bilbo has defeated the goblin")
            bilboHP = 100
            goblinHP = 75
            if goblinLVL > 5:
                print("You Win!")
                gamerun = "no"

            else:
                gamerun = input("Next LVL? [yes/no]: ")
            print("")
            print("-"*30)
            print("")
            
        else:
            print("Bilbo was defeated by the goblin")
            gamerun = "no"

    #Asks if they want to restart from lvl 1 after losing
    restart = input("Would you like to restart from lvl 1? [yes/no]: ")
    if restart.lower() == "yes":
        gamerun = "yes"
        bilboHP = 100
        goblinHP = 75
        bilboLVL =1
        goblinLVL = 1
        print("")
        print("")
        print("")
    else:
        gamerun = "no"

#---------------------------------------------------------------------------------------------
print("Thanks for playing")

