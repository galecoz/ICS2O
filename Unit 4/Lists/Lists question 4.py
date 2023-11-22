"""
Question 4
find mean median and mode from list
"""

import random

listRange = int(input("How many numbers would you like to be generated in this list?: "))
randomNum = 0
numbers = []
ave = 0
median = 0
mean = 0
mode = 0
number = 0
middle = 0
largest = 0

#Generates numbers
for i in range(listRange):
    randomNum = random.randrange(100)
    numbers.append(randomNum)
    ave += randomNum

#Sorts list
numbers.sort()


#median
if len(numbers) % 2 == 1:
    middle = listRange//2
    median = numbers[middle]

else:
    middle = listRange//2
    median = ((numbers[middle]+numbers[middle-1])//2)

#mean
mean = ave / listRange

#mode
for i in range(listRange):
    number = numbers.count(numbers[i])
    if number > largest:
        largest = number
        mode = numbers[i]


print("The median of this list is",median,"And the average of all the numbers is",mean,"And the mode is",mode)
