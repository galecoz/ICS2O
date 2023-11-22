"""
Question 5
"""

inventory = []
total = 0
aAble = True
bAble = True
cAble = True
dAble = True
e = True
action = 0

while e == True:
    total = len(inventory)

    if total == 0:
       bAble = False
       cAble = False
       dAble = False
       print("Your inventory is currently empty")
    else:
        print("There is",total,"items in your inventory")
        

    if total == 5:
        aAble = False
    
    print("Options:")
    if aAble = True:
        print("1. Add Item")
    if bAble = True:
        print("2. Delete Item")
    if cAble = True:
        print("3. Sort Inventory")
    if dAble = True:
        print("4. Print Inventory")
    print("5. Quit Program")

    while action != 
