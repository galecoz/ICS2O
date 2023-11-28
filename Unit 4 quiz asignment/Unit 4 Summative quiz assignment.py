"""
Name: Gabriel Dominato
Date: 
Version: 1.0
Discription: Create a quiz program that Contains 6 questions, 4 multiple choice (2 ordinary and 2 hard with 2 trys),
and 2 fill in the blanks that accepts upper and lower case
"""

import time, random, os
from colorama import init, Fore, Style
init(autoreset=True)

def clear_screen():
    os.system('cls')

#?Variables
quizRun = True
name = ""
response = ""
responses = []
count = 0
answers = ["a","b","c","d","e"]
grade = 0
average = 0
save = True
yeses = ["yes","yea","y","ye","yeah","mhm","yep"]
start = ""
correct = ""


#^Program
while quizRun == True:
    
    #^Intro To User
    print("")
    print(Style.NORMAL + Fore.LIGHTWHITE_EX+"Hello User. Welcome to the Clash of clans quiz.")
    print("There will be a Total of 6 questions with 4 multiple choice and 2 fill in the blanks. 2 of the multiple choice questions will be single attempt and 2 will have 2 attemps.")
    print("-"*30)

    start = input("<ENTER>")
    
    print("-"*30)
    name = input("Name: ")
    time.sleep(.5)
    while (not name.isalpha()):
        name = input("Name: ")
    
    time.sleep(1)
    clear_screen()
    #* Question 1 -------------------------------------------------------------------------------------------------------------------------------------
    print("Question 1: How many healers are typically used in a queen charge?")
    time.sleep(1.5)
    print("a. 2")
    time.sleep(.5)
    print("b. 10")
    time.sleep(.5)
    print("c. 1")
    time.sleep(.5)
    print("d. 5")
    time.sleep(.5)
    print("e. 7")
    time.sleep(1)
    response = input("Answer: ")

    while response.lower() not in answers:
        response = input("Answer: ")

    time.sleep(1)
    if response.lower() == "d":
        print("Correct")
        responses.append(1)
    else:
        print("Incorrect")
        responses.append(0)
    
    time.sleep(1)
    clear_screen()
    #* Question 2 -------------------------------------------------------------------------------------------------------------------------------------
    time.sleep(1.5)
    print("Question 2: How many earth quake spells does it take to destroy any level wall?")
    time.sleep(1.5)
    print("a. 5")
    time.sleep(.5)
    print("b. 4")
    time.sleep(.5)
    print("c. 3")
    time.sleep(.5)
    print("d. 2")
    time.sleep(.5)
    print("e. 1")
    time.sleep(1)
    response = input("Answer: ")

    while response.lower() not in answers:
        response = input("Answer: ")

    time.sleep(1)
    if response.lower() == "b":
        print("Correct")
        responses.append(1)
    else:
        print("Incorrect")
        responses.append(0)

    time.sleep(1)
    clear_screen()
    #! Question 3 -------------------------------------------------------------------------------------------------------------------------------------
    time.sleep(1.5)
    print("Question 3: What is the troop space for a hero?")
    time.sleep(1.5)
    print("a. 0")
    time.sleep(.5)
    print("b. 20")
    time.sleep(.5)
    print("c. 10")
    time.sleep(.5)
    print("d. 50")
    time.sleep(.5)
    print("e. 25")
    time.sleep(1)
    

    count = 0
    while count != 2:

        response = input("Answer: ")
        while response.lower() not in answers:
            response = input("Answer: ")
        time.sleep(1)
        if response.lower() == "e":
            print("Correct")
            count = 2

        
        if response.lower() != "e":
            print("Incorrect")
            count += 1
        
        if response.lower() != "e" and count != 2:
            time.sleep(.5)
            print("Question 3: What is the troop space for a hero?")
            time.sleep(1.5)
            print("a. 0")
            time.sleep(.5)
            print("b. 20")
            time.sleep(.5)
            print("c. 10")
            time.sleep(.5)
            print("d. 50")
            time.sleep(.5)
            print("e. 25")
            time.sleep(1)
    
    if response.lower() == "e":
        responses.append(1)
    else:
        responses.append(0)
    
    time.sleep(1)
    clear_screen()
    #! Question 4 -------------------------------------------------------------------------------------------------------------------------------------
    time.sleep(1.5)
    print("Question 4: When was Builder Base added?")
    time.sleep(1.5)
    print("a. 2014")
    time.sleep(.5)
    print("b. 2020")
    time.sleep(.5)
    print("c. 2017")
    time.sleep(.5)
    print("d. 2019")
    time.sleep(.5)
    print("e. On release")
    time.sleep(1)
    

    count = 0
    while count != 2:

        response = input("Answer: ")
        while response.lower() not in answers:
            response = input("Answer: ")
        time.sleep(1)
        if response.lower() == "c":
            print("Correct")
            count = 2

        if response.lower() != "c":
            print("Incorrect")
            count += 1

        if response.lower() != "c" and count != 2:
            time.sleep(.5)
            print("Question 4: When was Builder Base added?")
            time.sleep(1.5)
            print("a. 2014")
            time.sleep(.5)
            print("b. 2020")
            time.sleep(.5)
            print("c. 2017")
            time.sleep(.5)
            print("d. 2019")
            time.sleep(.5)
            print("e. On release")
            time.sleep(1)
    
    if response.lower() == "c":
        responses.append(1)
    else:
        responses.append(0)

    time.sleep(1)
    clear_screen()
    #~ Question 5 -------------------------------------------------------------------------------------------------------------------------------------
    time.sleep(1.5)
    print("Question 5: The ______ spell is the most recent spell added to Clash of Clans")
    time.sleep(1)
    response = input("Fill in the blank: ")
    time.sleep(1)
    if response.lower() == "recall":
        print("Correct")
        responses.append(1)
    else:
        print("Incorrect")
        responses.append(0)

    time.sleep(1)
    clear_screen()
#~ Question 6 -------------------------------------------------------------------------------------------------------------------------------------
    time.sleep(1.5)
    print("")
    print("Question 6: SUPERCELL tries to release a new town hall every ______ months")
    time.sleep(1)
    response = input("Answer: ")
    time.sleep(1)
    if response == "18":
        print("Correct")
        responses.append(1)
    else:
        print("Incorrect")
        responses.append(0)

    time.sleep(1)
    clear_screen()
    #^ Mark -------------------------------------------------------------------------------------------------------------------------------------
    for i in range(6):
        if responses[i] == 1:
            grade += 100
    average = grade / 6
    time.sleep(1)
    print("")
    print("Grade =",str("{0:0.1f}".format(average))+str("%"))
    time.sleep(.5)

    #^ Save -------------------------------------------------------------------------------------------------------------------------------------
    save = input("Would you like to save?: ")
    time.sleep(.5)
    if save in yeses:
        
        data = open('QuizResults.txt', 'a')
        data.write("Name: "  +name + ", Grade: "+ str("{0:0.1f}".format(average)) + "\n")
        
        for i in range(6):
            if responses[i] == 1:
                correct = "Correct"
            else:
                correct = "Incorrect"
            data.write("Q"+str((i +1))+": " + correct + "\n")
        data.write("----------------------------------"+"\n")
        
        data.close()
        print("Saving...")
        time.sleep(1)
        print("Saving..")
        time.sleep(1)
        print("Saving.")
        time.sleep(2)
        print("Saved")
    time.sleep(1)
    
    #^ Run again -------------------------------------------------------------------------------------------------------------------------------------
    start = input("Would you like to retake the quiz?: ")

    if start not in yeses:
        quizRun = False
        
    time.sleep(2)
    responses = []
    grade = 0
    average = 0
    
#^ End print -------------------------------------------------------------------------------------------------------------------------------------
time.sleep(.5)
clear_screen()
print("Thanks for trying the quiz")