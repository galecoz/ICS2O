phoneNum = int(input("imput your phone number and the computer will try to guess it and then tell you how many guesses it took to get it: "))
num = 1000000
count = 0

while num != phoneNum:
    num  = num +1
    count = count + 1

print("Your number is",num)
print("It took",count,"guesses")
               
