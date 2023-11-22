"""
Selection statements 2
"""

discount  = 0.7
hst = 0.14

gameP = float(input("What is the cost of the game you which to purchase?: "))
gameA = int(input("How many of these games are you purchasing?: "))
gamesC = gameP*gameA
discP = gamesC * discount
tax = 0
total = 0

if gameA > 20:
    print("Since you bought over 20 games, your bill will have a 30% dicsount on it")
    print("Subtotal:",discP)
    tax = discP * hst
    print("Tax:",tax)
    total = discP + tax
    print("Total:",total)

elif gameA <= 20:
    print("Subtotal:",gamesC)
    tax = gamesC * hst
    print("Tax:",tax)
    total = gamesC + tax
    print("Total:",total)

else:
    print("Invalid amount of games entered")
