"""
Selection question 5
"""

import time

age = int(input("Enter age: "))

for i in range(0,age,2):
    if age%2 == 0:
        print(i)

    else:
        i = i + 1
        print(i)
    time.sleep(.25)
