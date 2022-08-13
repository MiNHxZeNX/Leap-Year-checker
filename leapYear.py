year = int(input("Welcome to leap year checker!!\nPlease enter the year you want to check : "))
if year % 400 == 0:
    print(str(year) + " is a leap year")
elif year % 100 == 0:
    print(str(year) + " is not a leap year")
elif year % 4 == 0:
    print(str(year) + " is a leap year")
else:
    print(str(year) + "is not a leap year")
