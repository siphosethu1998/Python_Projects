"""
    This is a program that serves as module to the program calendar.py
    Author : Siphosethu Shumai
    Date : 2022/01/04
"""

def is_leap_year(year):
    # Given a year (a 4 digit number), returns true if it is a leap year, and false otherwise. 

    if year%4 == 0 or year%100 == 0 and year%400: 
        return True
    else:
        return False
    

def month_name(number):
    # Given the number of a month, returns the corresponding name. 1 is January, ..., 12 is December. 
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    return months[number-1]
    
def days_in_month(month_number, year):
    """ 
        Given a month (in the form of a number) and (4 digit) year, return the number of days in the
        month (accounting, in the case of February, for whether or not it is a leap year).
    """
    month_31 = ["January","March","May","July","August","October","December"] # list of all months that have 31 days

    month_30 = ["April","June","September","November"] # list of all months that have 30 days

    name_of_month = month_name(month_number)

    if name_of_month in month_31:
        return 31
    elif name_of_month in month_30:
        return 30
    elif name_of_month == "February" and is_leap_year(year):
        return 29
    else:
        return 28

def first_day_of_year(year):
    day = (1+ 5*((year-1)%4) + 4*((year-1)%100) + 6*((year-1)%400))%7

    return day

def first_day_of_month(month_number, year):
    """
        Given a month (in the form of a number) and (4 digit) year, return the number of the day on
            which the first of that month falls. 0 is Sunday, …, 6 is Saturday.
    """
    first_of_january = first_day_of_year(year)

    first_day_list = [first_of_january] # list for the first day of each month

    # putting the first day of each month in first_day_list except january which is already in there
    for index in range(11):
        first_day_list.append((first_day_list[index] + days_in_month(index+1, year))%7)

    return first_day_list[month_number-1]


def main():

    print(first_day_of_month(3,2022))

main()
    

