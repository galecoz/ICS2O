"""Header
Name:Gabriel
Date:28/09/2023
Version:1
Discription:Unit 1 Test
"""


import math


#Discription of the programs purpose for the user
print("This short program will ask you for the amount of minutes spent on different activites today and will tell you what % of the time spent on activites was spent doing what")
print("Aswell as how much you'd make if you earned 5$ per hour of healthy activities")
print("----------------------------------------------------------------------------")



#Inputs from user on time spent on each activites
homework = int(input("How many minutes today have you spent on Homework?:"))
phone = int(input("How many minutes today have you spent on your Phone or on social medias?:"))
eating = int(input("How many minutes today have you spent on Eating?:"))
videogames = int(input("How many minutes today have you spent playing Video Games?:"))
hobbies = int(input("How many minutes today have you spent on Hobbies such as sports and music?:"))
familytime = int(input("How many minutes today have you spent on Family Time?:"))




#Calculate the total time spent on actitivies and what % of that total time was spent on what activity
activitytime = homework + phone + eating + videogames + hobbies + familytime

thomework = homework / activitytime * 100
tphone = phone / activitytime * 100
teating = eating / activitytime * 100
tvideogames = videogames / activitytime * 100
thobbies = hobbies / activitytime * 100
tfamilytime = familytime / activitytime * 100

moneymade = math.floor((homework + eating + familytime) / 60) *5




#Ouput the total time spent on actitivies and the % spent on each, aswell as the money made from healthy actitivites
print("----------------------------------------------------------------------------")
print("The total time you spent on activities today was",activitytime,"minutes")
print("")

print(str("{0:.1f}".format(thomework))+str("%"),"of that total time was spent on homework")
print(str("{0:.1f}".format(tphone))+str("%"),"of that total time was spent on your phone/social medias")
print(str("{0:.1f}".format(teating))+str("%"),"of that total time was spent on eating")
print(str("{0:.1f}".format(tvideogames))+str("%"),"of that total time was spent playing video games")
print(str("{0:.1f}".format(thobbies))+str("%"),"of that total time was spent on hobbies")
print(str("{0:.1f}".format(tfamilytime))+str("%"),"of that total time was spent on family time")

print("----------------------------------------------------------------------------")
print("If you were making 5$ per hour spent on healthy activities today, then you'd have an extra",str(moneymade) +str("$"),"at the end of the day")
