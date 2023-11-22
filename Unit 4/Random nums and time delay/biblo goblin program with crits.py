bilboLVL = 1
goblinLVL = 1
hpLVLmultiplyerBilbo = 1.1
hpLVLmultiplyerGoblin = 1.2

bilboHP = 100
goblinHP = 50

bilboATK = 0
goblinATK = 0
bilboCC = 0
goblinCC = 0
bonusDMG = 0
click_count = 0

gamerun = "yes"
restart = "yes"
hits  = 0


startTime = 0
currentTime = 0

import random, time

#Allows game to be replayed if bilbo is defeated
while restart.lower() == "yes" :

    #Allows for multiple levels
    while gamerun == "yes":

        if bilboLVL != 1:
            bilboHP = bilboHP * (hpLVLmultiplyerBilbo*(bilboLVL - 1))

        if goblinLVL != 1:
            goblinHP = goblinHP * (hpLVLmultiplyerGoblin*(goblinLVL - 1))
 
        #The game
        while bilboHP > 0 and goblinHP > 0:


            #HP statements
            print("LVL",goblinLVL,"Goblin HP: ",str("{0:0.1f}".format(goblinHP)))
            print("LVL",bilboLVL,"Bilbo HP: ",str("{0:0.1f}".format(bilboHP)))
            print("")
            time.sleep(1)
            #Calculates crit chance
            bilboCC = random.randint(1,4)
            goblinCC = random.randint(1,8)


            #decides between if its a crit or not and calculates and deals dmg
            if goblinCC == 1:                                            #goblin
                goblinATK = random.randint(10,20) *  2
                print("The goblin hit a CRITICAL  and dealt",goblinATK,"damage to bilbo")

            else:                                                       #goblin
                goblinATK = random.randint(10,20)
                print("The goblin dealt",goblinATK,"damage to bilbo")
            print("")

            bilboHP = bilboHP - goblinATK
            time.sleep(1)

            #use an input calculator and let the player spam to increase their dmg range
            click_count = 0
            print("To increase bilbo's atk range, Spam enter for 5secs!")



            startTime = time.time()
            hits = 0
           

            while currentTime != round(startTime + 5):
                currentTime = round(time.time())
            
                hits = input("spam")
                
                




            #Bonus dmg calculator
            bonusDMG = 0
            bonusDMG = 0.5 * click_count


            if bilboCC == 1:                                             #bilbo
                bilboATK = (random.randint(10,20)+ bonusDMG *  2 )
                print("Bilbo hit a CRITICAL  and dealt",str("{0:0.1f}".format(bilboATK)),"damage to the goblin")

            else:                                                        #bilbo
                bilboATK = (random.randint(10,20) + bonusDMG)
                print("Bilbo dealt",str("{0:0.1f}".format(bilboATK)),"damage to the goblin")
            print("-"*30)

            goblinHP = goblinHP - bilboATK
            time.sleep(4)

        #tells if biblo or the goblin 
        if bilboHP > 0:
            print("Bilbo has defeated the goblin")
            bilboHP = 100
            goblinHP = 50
            gamerun = input("Next LVL? [yes/no]: ")
            print("")
            print("-"*30)
            print("")
            bilboLVL = bilboLVL + 1
            goblinLVL = goblinLVL + 1
        else:
            print("Bilbo was defeated by the goblin")
            gamerun = "no"
        
    restart = input("Would you like to restart from lvl 1? [yes/no]: ")

print("Thanks for playing")
