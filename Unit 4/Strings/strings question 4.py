"""
question 4
"""

import random

word = "apple"
ogword = word
scramble = ""
randint = 0
wordCount = len(word)
letter = ""
guess = ""
tries = 0

for i in range(wordCount):
    wordCount = len(word)

    randint = random.randrange(wordCount)
 
    letter = word[randint]
  
    scramble = scramble+letter
   
    word = word.replace(str(word[randint]),"")

print(scramble)

while tries != 3:
    guess = input("What is the original word?: ")
    if guess == ogword:
        tries = 3

    else:
        print("wrong")
        tries = tries + 1

if guess == ogword:
    print("Correct")

else:
    print("Womp womp, original:",ogword)
