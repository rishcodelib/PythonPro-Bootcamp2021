# Conditional Statements in Python 
# ?     If (Condition) {
# ?     . . .
# ?     }
# ?     else {
# ?     . . .
# ?     }
# ? INDENT MATTERS

height = int(input("Enter the number "))
if (height % 2) == 0:
    print ("Even number")
else:
    print("Odd number")

#  * * Nested If-else in Python: for elseif in python we use elif

if height >20:
    print ('height is above 20')
elif height ==20:
    print("height is 20")
elif height <20:
    print("height is small than 20")
else:
    print("nothing")