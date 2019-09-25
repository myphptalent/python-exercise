#
# Example file for working with timedelta object
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


def main():
   # Construct a basic timedelta and print it
   print(timedelta(days=365, hours=5, minutes=1))

   # Print today's date
   now = datetime.now()
   print("Today is :"+ str(now) )





if __name__ == "__main__":
    main()