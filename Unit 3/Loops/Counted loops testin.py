"""
5
"""

total = 0
rounds = int(input("How many numbers are you going to input? : "))

for rounds in range(rounds):
    inp = int(input("Enter number: "))
    total = total + inp
    print("Current sum:",total)
    print("")

print("final sum:",total)
