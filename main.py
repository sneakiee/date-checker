#inputs for d/m/y in number
day = int(input("Enter day: "))
month = int(input("Enter month digit: "))
year = int(input("Enter year: "))

#defining sum as global variable
sum = 0

#checks month and sets the key number according to month
def monthChecker():
    #if not leap year
    if year % 4 != 0:
        if month == 1 or month == 10:
            keyNum = 1
        elif month == 2 or month == 3 or month == 11:
            keyNum = 4
        elif month == 4 or month == 7:
            keyNum = 0
        elif month == 5:
            keyNum = 2
        elif month == 6:
            keyNum = 5
        elif month == 8:
            keyNum = 3
        elif month == 9 or month == 12:
            keyNum = 6
    #if leap year
    else:
        if month == 1:
            keyNum = 0
        elif month == 2:
            keyNum = 3
        elif month == 10:
            keyNum = 1
        elif month == 3 or month == 11:
            keyNum = 4
        elif month == 4 or month == 7:
            keyNum = 0
        elif month == 5:
            keyNum = 2
        elif month == 6:
            keyNum = 5
        elif month == 8:
            keyNum = 3
        elif month == 9 or month == 12:
            keyNum = 6
    
    return keyNum

#checks which century and changes sum based off century
def yearChecker():
    if year >= 2000 < 2100:
        x = sum - 1
    elif year < 1900:
        x = sum + 2
    elif year < 1800:
        x = sum + 4
    else:
        pass
    
    return(x)

#checks which day of the week it is through remainder
def dayChecker():
    x = sum % 7

    if x == 0:
        day = "Saturday"
    elif x == 1:
        day = "Sunday"
    elif x == 2:
        day = "Monday"
    elif x == 3:
        day = "Tuesday"
    elif x == 4:
        day = "Wednesday"
    elif x == 5:
        day = "Thursday"
    elif x == 6:
        day = "Friday"
    
    return day

#get the key number
keyNum = monthChecker()

#get last 2 numbers
lastTwo = year % 100

#calculate the sum
sum = lastTwo + int((lastTwo / 4)) + day + keyNum
sum = yearChecker()

#get the day of the week and output
DOTW = dayChecker()
print(DOTW)