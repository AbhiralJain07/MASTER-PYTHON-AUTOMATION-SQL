# Basics of Date and time module:

from datetime import datetime

## current date and time
presentime = datetime.now()
print("today is :" , presentime)

## get individual time 
presentime = datetime.now()
print(presentime.year , presentime.month , presentime.day)
print(presentime.hour , presentime.minute , presentime.second)

#formatting date and time -- using strftime
presenttime = datetime.now()
print(presenttime.strftime ("%d - %m - %Y"))
print(presenttime.strftime("%H - %M - %S"))