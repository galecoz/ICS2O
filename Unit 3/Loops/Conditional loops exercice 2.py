"""
Counted loops question 2
"""

import time


#Ask user for countdown durration and what they would like the count down to say ast the end
durration = int(input("From what number would you like to count down from?: "))
end = input("What phrase would you like to end the countdown with?: ")

endCount = len(end)

#Printing countdown and end 
for i in range(durration,0,-1):
    print(i,end = " ")
    time.sleep(.5)
    
for letter in end:
    print(letter,end = "")
    time.sleep(.25)
