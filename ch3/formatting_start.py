#
# Example file for formating time and date output
#

from datetime import datetime


def main():
    # Times and dates can be formatted using a set of predefined string
    # Control codes
    now = datetime.now()

    #########Date formatting#############
    # %y %Y - year, %a %A - weekday, %b %B - Month, %d - Day of month
    print(now.strftime("The current year is: %Y" ))













if __name__ == "__main__":
    main()