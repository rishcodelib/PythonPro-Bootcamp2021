# Code Challenge in Python
# Love Calculator : TRUE LOVE Concept. 

name1 = input("Enter the Name of person 1 \n")
name2 = input("Enter the Name of person 2 \n")

# lower function is used to convert whole string into lowercase.
# Count() function will tell how many times letter comes into a string.


# Check TRUE and LOVE
name1 = name1.lower()
name2= name2.lower()
name = (name1 + name2)
T = name.count("t")
R = name.count("r")
U = name.count("u")
E = name.count("e")
TRUE = T + R + U + E

L = name.count("l")
O = name.count("o")
V = int(name.count("v"))
e = name.count("e")
LOVE = L + O + V + e
TRUE = str(TRUE)
LOVE = str(LOVE)
score = TRUE + LOVE
score = int(score)

if score < 10 or score > 90:
    print (f"Your score is  {score} you go toghether like coke and mentos")
elif score >= 40 and score <= 50:
    print (f"Your score is  {score}  you are alright together.")
else:
    print (f"Your score is  {score} ")