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
count = 0
answers = ["a","b","c","d","e"]
grade = 0

#^Intro To User

print("Hello User. Welcome to the Clash of clans quiz.")
print("There will be a Total of 6 questions with 4 multiple choice and 2 fill in the blanks. 2 of the multiple choice questions will be single attempt and 2 will have 2 attemps>.")
print("-"*30)

#^Program
while quizRun == True:
    name = input("Name: ")
    time.sleep(.25)
    
    
    #* Question 1
    print("")
    print("Question 1: How many healers are typically used in a queen charge?")
    print("a. 2")
    print("b. 10")
    print("c. 1")
    print("d. 5")
    print("e. 7")
    
    response = input("Answer: ")

    while response.lower() not in answers:
        response = input("Answer: ")

    if response == "d":
        print("Correct")
        responses.append(1)
    else:
        print("Incorrect")
        responses.append(0)
    
    #* Question 2 
    time.sleep(.25)
    print("")
    print("Question 2: How many earth quake spells does it take to destroy any wall?")
    print("a. 5")
    print("b. 4")
    print("c. 3")
    print("d. 2")
    print("e. 1")
    
    response = input("Answer: ")

    while response.lower() not in answers:
        response = input("Answer: ")

    if response == "b":
        print("Correct")
        responses.append(1)
    else:
        print("Incorrect")
        responses.append(0)

    
    #! Question 3
    time.sleep(.25)
    print("")
    print("Question 3: What is the troop space for a hero?")
    print("a. 0")
    print("b. 20")
    print("c. 10")
    print("d. 50")
    print("e. 25")
    
    response = input("Answer: ")

    count = 0
    while count != 2:
        while response.lower() not in answers:
            response = input("Answer: ")
    
        if response == "e":
            count = 2

        else:
            print("Incorrect")
            count += 1
        
            time.sleep(.25)
            print("")
            print("Question 3: What is the troop space for a hero?")
            print("a. 0")
            print("b. 20")
            print("c. 10")
            print("d. 50")
            print("e. 25")
    
    if response == "e":
        print("Correct")
        responses.append(1)
    else:
        print("Incorrect")
        responses.append(0)
    
    
    #! Question 4 
    time.sleep(.25)
    print("")
    print("Question 4: When was Builder Base added?")
    print("a. 2014")
    print("b. 2020")
    print("c. 2017")
    print("d. 2019")
    print("e. On release")
    

    count = 0
    while count != 2:

        response = input("Answer: ")
        while response.lower() not in answers:
            response = input("Answer: ")
    
        if response == "":
            print("Correct")
            count = 2

        else:
            print("Incorrect")
            count += 1
        
            time.sleep(.25)
            print("")
            print("Question 4: When was Builder Base added?")
            print("a. 2014")
            print("b. 2020")
            print("c. 2017")
            print("d. 2019")
            print("e. On release")
    

    if response == "":
        print("Correct")
        responses.append(1)
    else:
        print("Incorrect")
        responses.append(0)


    #~ Question 5
    time.sleep(.25)
    print("")
    print("Question 5: The ______ spell is the most recent spell added to Clash of Clans")
    
    response = input("Fill in the blank: ")

    if response.lower() == "recall":
        print("Correct")
        responses.append(1)
    else:
        print("Incorrect")
        responses.append(0)

#~ Question 6
    time.sleep(.25)
    print("")
    print("Question 6: SUPERCELL tries to release a new town hall every ______ months")
    
    response = input("Answer: ")

    if response == "18":
        print("Correct")
        responses.append(1)
    else:
        print("Incorrect")
        responses.append(0)

    #^ Mark
    for i in range(6):
        if responses[i] == 1:
            grade += 100

    