"""
Name: Gabriel Dominato
Date: ------
Version: 1.0
Discription: Create a quiz program that Contains 6 questions, 4 multiple choice (2 ordinary and 2 hard with 2 trys),
and 2 fill in the blanks that accepts upper and lower case
"""

import time, random


#?Variables
quizRun = True
name = ""
response = ""
responses = []
    


#^Intro To User

print("Hello User. Welcome to the --- quiz.")
print("There will be a Total of 6 questions with 4 multiple choice and 2 fill in the blanks. 2 of the multiple choice questions will be single attempt and 2 will have 2 attemps>.")
print("-"*30)

#^Program
while quizRun == True:
    name = input("Name: ")
    time.sleep(.25)
    print("")
    print("Question 1: ")
    print("1. ")
    print("2. ")
    print("3. ")
    print("4. ")
    print("5. ")
    
    while response != "1" or "2" or "3" or "4" or "5":
        response = int(input("Answer: "))
    responses.append(response)

    
    
    