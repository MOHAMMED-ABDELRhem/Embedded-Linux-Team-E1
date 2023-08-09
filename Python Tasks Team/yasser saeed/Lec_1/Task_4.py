import calendar
#assigne the value of a year in a variable y
y = int(input("enter the year : "))
#assigne the value of the month in a variable m
m = int(input("enter the month : "))
#printing the calendar by using the calendar.month in-built function provided by python
print(calendar.month(y, m))