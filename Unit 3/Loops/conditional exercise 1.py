"""
Conditional loops exercise 1
"""

#Constant
namesList = []
ext = ""
answer = ""


#Getting names
while ext.lower() != "exit":
    ext = str(input("Enter name: "))
    namesList.append(str(ext))
    


#Count number of names in list and output that number
namesList.remove("exit")
listCount = len(namesList)
print("You added ",listCount,"names to the system")


#Asking if user wants to see list
if listCount > 0:
    answer = input("Would you like to see the names added to the system? [yes/no]: ")
    if answer.lower() == "yes":
        print(namesList)

print("")
print("End")

