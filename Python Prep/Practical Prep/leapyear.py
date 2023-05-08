
# to be a leap year the number of year should satify the following 2 conditions

# 1 year should be a multiple of 400
# 2 year should be a multiple of 4 but not of 100

def isleap(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


print(isleap(2005))
# returns true if year is leap else returns false
