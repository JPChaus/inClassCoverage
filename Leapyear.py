#Jackson E. Rollins
#4/25/2021

#Program that asks for a year from the user and then determines if it is a leap year or not.
#Repatedly asks the user for a new number if the number given is not a positive integer

def main():
    while True:
        try:
            year = int(input("Please enter a year. Positive integer values only: "))
            if(year < 0):
                raise ValueError
            break
        except ValueError:
            print("Invalid input!")
    
    print(isLeapYear(year))

def isLeapYear(year):
    if (year%400 == 0):
        return ("% s is a Leap Year." % year)
    elif (year%100 == 0):
        return ("% s is not a Leap Year." % year)
    elif (year%4 == 0):
        return ("% s is a Leap Year." % year)
    else:
        return ("% s is not a Leap Year." % year)

if __name__ == '__main__':
    main()