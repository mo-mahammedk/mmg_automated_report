#!/usr/bin/python
import datetime

friday = datetime.date.today()
while friday.strftime('%a') != 'Fri':
    friday += datetime.timedelta()
# print (friday)
def foo(myDate):
    date_suffix = ["th", "st", "nd", "rd"]

    if myDate % 10 in [1, 2, 3] and myDate not in [11, 12, 13]:
        return date_suffix[myDate % 10]
    else:
        return date_suffix[0]
        
worded = friday.strftime(f'%d{foo('%d')} %B %Y')
# print(worded)
