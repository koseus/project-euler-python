def is_leap_year(year):
    """Check if a year is a leap year"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    """Return the number of days in the given month"""
    if month == 2:
        return 29 if is_leap_year(year) else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def solve():
    """
    How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
    """
    # Start from 1 Jan 1900 (Monday)
    day_of_week = 1  # 0 = Sunday, 1 = Monday, ..., 6 = Saturday
    sunday_count = 0
    
    # Process each year
    for year in range(1900, 2001):
        # Process each month
        for month in range(1, 13):
            # Check if it's a Sunday on the first of the month
            if year >= 1901 and day_of_week == 0:
                sunday_count += 1
            
            # Move to the first day of next month
            day_of_week = (day_of_week + days_in_month(year, month)) % 7
    
    return sunday_count

    print(solve())