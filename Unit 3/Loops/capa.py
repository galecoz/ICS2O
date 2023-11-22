"""
Pasnoword
"""

count = 1
password = "CHEESE"
uInp = input("Enter Password: ")

while uInp.upper() != password:
    print("Inccorrect")
    count =  count + 1
    uInp = input("Enter Pasword: ")
    
    if count == 10:
        uInp = "CHEESE"
        print("Ran out of attempts")

print("You got it in",count,"attempts")
            

 
       
