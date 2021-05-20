#Jackson E. Rollins
#4/25/2021

#Program that asks for a year from the user and then determines if it is a leap year or not.
#Repatedly asks the user for a new number if the number given is not a positive integer

while True:
    try:
        year = int(input("Please enter a year. Positive integer values only: "))
        if(year < 0):
            raise ValueError
        break
    except ValueError:
        print("Invalid input!")

if (year%400 == 0):
    print("% s is a Leap Year." % year)
elif (year%100 == 0):
    print("% s is not a Leap Year." % year)
elif (year%4 == 0):
    print("% s is a Leap Year." % year)
else:
    print("% s is not a Leap Year." % year)