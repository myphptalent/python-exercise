#
# Example file for working with date informations
#

from datetime import date
from datetime import time
from datetime import datetime

def main():
    # ## DATE OBJECTS
    # # Get today's date from the  simple today() method from the date class
    # today = date.today()
    # print("Today's date is", today)
    
    # # Print out the date's individual components
    # print("Date components: ", today.day, today.month, today.year)
    
    # # Retrieve today's weekday (0=Monday, 6=Sunday)
    # print("Today's weekday is ", today.weekday())
    # days = ["Mon","Tues", "Wed", "Thu", "Fri", "Sat", "Sun"]
    # print("Which is a : ", days[today.weekday()])


    ## DATETIME OBJECT
    # Get today's date from datetime class
    today = datetime.now()
    print("The current date time is: ", today)

    # Get the current time from datetime class
    time = datetime.time(datetime.now())
    print("The current time is : ", time)



if __name__ == "__main__":
    main()
