import datetime as dt
import time

print("Welcome to the birthday countdown!")

try:
    year = int(input("Which year were you born in?\n"))
    month = int(input("Which month were you born in? (1 for January, 2 for February and so on)\n"))
    day = int(input("Which day of that month?\n"))

    try:
        weekday_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                         'Friday', 'Saturday', 'Sunday']

        date_birth = dt.datetime(year, month, day)

        leap_year_bday = 0

        if date_birth.day == 29 and date_birth.month == 2:
            leap_year_bday = 1
            print('Your birthday is a leap year day.')

        weekday_num = date_birth.weekday()

        print()
        print("You were born on a...", end=' ')
        print(weekday_names[weekday_num])

        current_time = dt.datetime.now()
        thisyear = current_time.year

        if date_birth < current_time:

            try:
                thisyear_bday = dt.datetime(thisyear, month, day)

                if thisyear_bday > current_time:
                    next_bday = thisyear_bday
                    print('Your next birthday will be this year:')

                else:
                    if leap_year_bday != 1:
                        next_bday = dt.datetime(thisyear + 1, month, day)
                    else:
                        next_bday = dt.datetime(thisyear + 4, month, day)

                    print('Your next birthday will be next year:')

            except:
                # This year not a leap year
                next_bday = dt.datetime(
                    thisyear + (4 - thisyear % 4),
                    month,
                    day
                )

            print(next_bday)

            weekday_num = next_bday.weekday()

            print()
            print("Your next birthday will be on a ... ", end=' ')
            print(weekday_names[weekday_num])

            diff = current_time - date_birth
            a = diff.days // 365

            print("You are", a, "years old as of now.")


            if year >= 1946 and year <= 1964:
                print('You are a part of the generation of baby boomers.')
            elif year >= 1965 and year <= 1980:
                print("You are a part of Generation X.")
            elif year >= 1981 and year <= 1996:
                print("You are a part of Generation Y.") 
            elif year >= 1997 and year <= 2009:
                print("You are a part of Generation Z.")
            elif year >= 2010 and year <= 2024:
                print('You are a part of Generation Alpha.')
            elif year >= 2025 and year <= 2036:
                print("You are a part of Generation Beta.")

            while next_bday > current_time:

                current_time = dt.datetime.now()
                dd = next_bday - current_time

                days_left = dd.days
                total_seconds_left = dd.seconds

                total_seconds = total_seconds_left % 60
                total_minutes_left = total_seconds_left // 60
                minutes_left = total_minutes_left % 60
                hours_left = total_minutes_left // 60

                print(
                    "Your next birthday is in", days_left, "days", hours_left, "hours,", minutes_left, "minutes, and", total_seconds, "seconds.", end='\r')

                time.sleep(1)

        else:
            print("Future birthdate entered. Please try again.")

    except:
        print("Invalid date. Please try again.")

except:
    print("It looks like there were incorrect values entered. Please try again.")
