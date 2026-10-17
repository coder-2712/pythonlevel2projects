import datetime as dt
import time

print("Welcome to the birthday countdown!")
year = int(input("Which year were you born in?\n"))
month = int(input("Which month were you born in? (1 for January, 2 for Febuary and so on)\n"))
day = int(input("Which day of that month?\n"))

weekday_names = ['Monday', 'Tuesday','Wednesday', 'Thursday','Friday','Saturday','Sunday']

date_birth = dt.datetime(year, month, day)
weekday_num = date_birth.weekday()

print()
print("you were born on a...", end = ' ')
print(weekday_names[weekday_num])

current_time = dt.datetime.now()
thisyear = current_time.year
thisyear_bday = dt.datetime(thisyear,month,day)
if thisyear_bday>current_time:
    next_bday = thisyear_bday
    print('Your next birthday will be this year:')
else:
    next_bday = dt.datetime(thisyear+1,month,day)
    print('Your next birthday will be next year:')

print(next_bday)


weekday_num = next_bday.weekday()

print()
print("your next birthday will be on a ... ", end = ' ')
print(weekday_names[weekday_num])

while next_bday>current_time:

    current_time = dt.datetime.now()
    dd = next_bday - current_time
    days_left = dd.days
    total_seconds_left = dd.seconds

    total_seconds = total_seconds_left % 60
    total_minutes_left = total_seconds_left // 60
    minutes_left = total_minutes_left % 60
    hours_left = total_minutes_left // 60
    print("Your next birthday is in", days_left, "days,", hours_left, "hours,", minutes_left, "minutes, and", total_seconds, "seconds.", end = "\r")
    time.sleep(1)