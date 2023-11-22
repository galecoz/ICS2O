"""Header
Name:Gabriel
Date:
Version:
Discription:
Algorythm:
1=ask user for the runners starting time and finishing time aswell as the length of the race in km and time in hours on the 24hour clock
2=calculate the runners avarage speed by finding the time it took to run the race and devide it by the distance
3=output the runners speed to the user
"""


#info for user
print("Hello user, this program will calculate the running speed of a runner after asking you for the distance of the race (km), and the starting and finishing times in hours then minutes on the 24h clock")
print("")
print("-"*30)


#Variables/inputs (Ask user for the starting/finishing time/distance of the race
startH = float(input("When did the race start? (hours):"))
startM = float(input("When did the race start? (minutes):"))
print("")
finishH = float(input("When did the runner finish the race? (hours):"))
finishM = float(input("When did the runner finish the race? (minutes):"))
print("")
distance = float(input("What is the distance of the race in km?:"))


#Calculate the runners avarage speed
timeRanH = finishH - startH
timeRanM = finishM - startM

#Changing the minutes to a base 100 scale from a base 60 scale to calculate speed
speed = distance / ((timeRanH*100 + timeRanM*1.66666667)/100)


#Ouput the runners speed
print("-"*30)
print("The runners average speed durring this race would have been "+str("{0:.2f}".format(speed))+str("kmph"))
