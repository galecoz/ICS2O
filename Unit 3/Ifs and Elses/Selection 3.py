"""
Selection Statements 3
"""

number = 50
userinp = int(input("Enter number: "))
count = 1
num = 0

while userinp != number:
    count = count +1
    if count > 10:
        num = num + 1
        break

    if userinp > number:
        print("Lower")

    else:
        print("Higher")

    userinp = int(input("Enter number: "))
      
if num == 1:
    print("Out of attemtps")

else:
    print("Correct")
