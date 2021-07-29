# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.


weight = int(input("enter your weight in kg: \n"))
height = float(input("enter your height in m:\n "))

calc = weight /( height * height)
print (calc)
