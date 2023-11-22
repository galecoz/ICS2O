"""
Selection 4
"""

#Modifing the largest number program to also find the smallest number

number  = 0

number = int(input("Enter a number: "))
largest = number
smallest = number

for i in range(9):
    number = int(input("Enter a number: "))

    if number > largest:
        largest = number

    elif number < smallest:
        smallest = number

print("The largest number is",largest)
print("The smallest number is",smallest)
