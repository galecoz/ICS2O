"""
Conditional loops exercise 4
"""

import time

coins = 20
raven = 3
magicM = 1.5


for i in range(365):
    coins = coins*magicM - raven
    print("Coins:",coins)


for i in range(365):
    print("Day:",str(i+1))
    print("You have",coins,"coins and you use the magic machine and the crow flies down a and steals 3 coins")
    coins = coins*magicM - 3
    print("At the end of the day you have",str("{0:0.2f}".format(coins)),"coins")
    time.sleep(2)
    print("")
