# Banker Roulette Code Challenge
# Choose Random Names from a list of Names like a Toss
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

length = len(names)



choice = random.randint(0,length-1)

print(f"is going to buy  the meal today: {names[choice]}")

# or Shortcut Alternative approach 
# random.choice will randomly get from list.

pay = print(f"He will PAY YOU : {random.choice(names)}")