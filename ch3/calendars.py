# Example file for working with calendar

#import the calendar module

import calendar

#Create a plain text calendar

# c = calendar.TextCalendar(calendar.SUNDAY)
# st = c.formatmonth(2019,9,0,0)
# print(st)

#Create a HTML formated calendar

hc = calendar.HTMLCalendar(calendar.SUNDAY)
st = hc.formatmonth(2019,9)
print(st)



