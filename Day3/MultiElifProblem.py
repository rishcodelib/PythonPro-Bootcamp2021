# Rollercoster problem 

height = int(input("Enter height in cm?"))
bill = 0
if height >=120:
    print ("you can ride the roller coster")
    age= int(input("what is your age"))
    if age <12:
        bill =5
        print("Child ticket are $5")
    elif age <18:
        bill = 7  
        print("youth ticket are $7")
    elif age > 18:
        bill = 12
        print("adult ticket are $12")
# Space for sepration and check indentation.
    wants_photo =  input("do  you wante a photo? Y or N ")
    if wants_photo =="Y":
        bill += 3
# Space for sepration. 
    print(f"your bill value is: {bill}")

else:
    print("your cannot ride roller-coster")

# Always check indentation, 