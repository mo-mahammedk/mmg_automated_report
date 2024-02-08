# !/usr/bin/python
import datetime

friday = datetime.date.today()

while friday.strftime('%a') != 'Fri':
    friday += datetime.timedelta(1)
    # print (friday)
    worded = friday.strftime('%d %B %Y')
    # print(worded)
