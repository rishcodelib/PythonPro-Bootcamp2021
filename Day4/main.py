# Randomisation in Python. 
# Ramdom Module in Py.
# Mersenne Twister is the Approach By Python to Generate Random Number

import random

a = random.randint(1,10)
print(a)


# How to import from another file. 
# Create a File with FILENAME.py
# Use import FILENAME.
# print(FILENAME.variableName)
# ?  Example - - - 

import SampleModule
print("Example of importing a number from another file using Module import .")
print(SampleModule.rishabh)


# ? - - - 

# Random Floating Point  NumberL doesnot include last limit i.e 1
# for between 0 and 1
b = random.random()  
print(b)

# How to make random float number to go beyond 0 to 1
# ? Just Multiply by any integer Example::

print(b*10)
print(b*2)

# ? ----

