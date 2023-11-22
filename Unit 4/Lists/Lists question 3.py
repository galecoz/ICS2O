"""
question 3
"""

import random

numbers = []
number = 0 
search = 0
true = True
places = []
place = 0
inL = 0

for i in range(100):
    number = random.randint(1,100)
    numbers.append(number)



while true == True:
    search = int(input("What Number from 1-100 would you like to find?: "))
    inL = numbers.count(search)

    if inL < 1:
        print("That number is not in the list. Please try another")

    else:
        while numbers.count(search) > 0:
                place = numbers.index(search)
                places.append(place)
                del numbers[place]      
        true = False



print("There is a",search,"at",places,"In the list")


