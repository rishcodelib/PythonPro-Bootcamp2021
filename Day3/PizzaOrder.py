print("Welcome to python Pizza Deliveries!")

menu= " \n Small Pizza $15 \n Medium Pizza $20 \n Large Pizza $25 \n -- \n Pepporoni on Small Pizza : +$2 \n Pepporoni on Medium /Large Pizza : +$3 \n Extra Cheese on Pizza : +$1 "
bill =0
print(menu)
size = input("what side of Pizza you want? S , M, L ")
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill =25
else :
    print("Please Enter a Valid Input.")
add_Pepperoni = input("would you like to add pepperoni? Y or N ")
if add_Pepperoni == "Y" and size == "S":
    bill += 2
elif add_Pepperoni == "Y" and size == "M" or size == "L":
    bill += 3

extra_cheese = input("would you like to have extra cheese? Y or N ")
if extra_cheese == "Y":
    bill+= 1

print(f"Your bill is {bill}")
