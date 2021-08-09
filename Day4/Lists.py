# Python LIST 
# Datastructure
# Storing data is a List

# Grouped Data in a List.
# Ordered Data is Queue.


Countries = ["USA","INDIA","Shrilanka", "bangladesh" ]

print(Countries)
print(Countries[0])
print(Countries[2])

# How to updaate?
Countries[0] = "United States of America"
print (Countries)

# How to add in the list? 

Countries.append("China")

print(Countries)


# How to actually add another list to the existing list?
Countries.extend(["Europe","UK","Singapore","Thiland"])

print(Countries)


# Split Method:
# Used to Split a given String into List Item based on specific (,) Identifier 

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
print(names)

# 