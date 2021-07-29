# DataTypes in Python: Strings ,Integers, Float and Boolean

# # Sub-scripting method to pull out 1 character from a string.

#  Print 1st character of string

print("Hello"[0])

# String Concatination in Py
print("123" + "123" )
#  We Canot concatinate string with integer 
# ! age =12
# ! print ("your age " + age + 'is ') 
# This will give Type Error

# Addition using print in PY
print(123 +23)

# How to seprate numbers in python eg (100,001,11)
print(100_001_11)

# Boolean True / False

num_char = len("Hello")

# type check in python
print(type(num_char))

#type Casting in python
new_num_char = str(num_char)

print(new_num_char)


a= str(123)
print(type(a))




# Mathematical operations: 
print (2 + 5)
print (2 - 2)
print (2 * 2)
# Divide Will give output in Float
print (2 / 2) 

# Exponential powers
print (2 ** 2)



#? Order of calculations 
# PEMDAS-LR
# Parantheses ()
# Exponenets **
# Multiply and Division * /
# Add & Substract + -

# LR : Left to Right

# 
print (3 * 3 + 3 / 3 -3)
# Output: 7.0

# ############
# ? BMI Calculation Program:: 
# ############

# ? Number Manupulation 
# 
# Simple Divide
print (8/3)
# Ans: 2.6666666666666665
# 
# Round to a Whole no.
print (round(8/3)) 
# Ans:= 3
# 
# Round to 2 Decimal Places, 
print (round(8/3, 2)) 
#  Ans:  = 2.67
# 
#Floor Division 
print ( 8 // 3) 
# Answer: 2
# 
#? F Strings in Python :
# Converts all variable into string
score = 0
height =1.8
isWining = True
# f-string
print (f"your score is {score}, your height is  {height} and your are wining is : {isWining} ")
# Points :
# Using f in front of sting is Important
# 