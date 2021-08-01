# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.


weight = int(input("enter your weight in kg: \n"))
height = float(input("enter your height in m:\n "))

calc = round(weight /( height ** 2))

if calc <18.5:
    print(f"you are UNDERWEIGHT {calc}" )
elif calc < 25:
    print (f"Normal Weight {calc}")
elif calc < 30:
    print(f"over weight {calc}")
elif calc < 35:
    print(f"obese {calc}")
else:
    print(f"clinically obese {calc}")