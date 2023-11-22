"""
Coutned loops question #3
"""

import time

balance = 1000
intRate = 0.06
interest = 0

year = int(input("What year is it currently?: ")) -1

for i in range(10):
    print("")
    year = year + 1
    print("Year:",year)
    print("Balance:",str("{0:.2f}".format(balance)))

    interest = balance*intRate
    time.sleep(.5)
    print("Interest:",str("{0:.2f}".format(interest)))

    balance = balance + interest
    time.sleep(.5)

    print("End Balance:",str("{0:.2f}".format(balance)))
    time.sleep(2.5)
    print("")
    print("-"*30)
   
