# How to check Leap Year:
# 
# ? On every year that is evenly divisible by 4
# ! except every year that is evenly divisible by 100
# * unless the year is also evenly divisible by 400

year = int(input("Enter the year"))

isLeap = (year/4) and (year/100)

if year%4 == 0:
    if year%100 ==0:
        if year%400 ==0:
            print("LEAP year")
        else:
            print("not a LEAP year")
    else:
        print("LEAP Year")
else:
    print("not a LEAP year")