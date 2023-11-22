"""
Qestion 1
"""
#Data from file
studentMarks = open('StudentMarks.txt')

#Variables
names = []
mark = 0
name = ''
line = ''
totalMarks = 0
average = 0
averages = []
inputing = ''

#10 Students
for i in range(10):
    line = studentMarks.readline().split() #Reads the line

    #Resets variables
    average = 0 
    totalMarks = 0

    #Takes name from line and adds it to a list
    name = line[0]
    names.append(name)

    #4 times for each mark and adds it to an acumilator
    for i in range(4):
        mark = int(line[i+1])
        totalMarks += mark

    #Calculates average and adds it to a list
    average = totalMarks // 4
    averages.append(average)


#Prints Students names and averages using the lists in a table
print("Student","\t","Average")
for i in range(10):
    print(names[i],"\t\t",averages[i])


#-----------------------------------------------------------------------------
"""
adds data to new file
"""

file = open('StudentAverages', "w")

for i in range(10):
    file.write(names[i] + " Average:" + str("{0:0.2f}".format(averages[i])) +"%\n")
file.close()
    
