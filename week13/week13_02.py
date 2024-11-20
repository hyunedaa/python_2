#week13_02.py
#id:202444079
#name:Kwon hyun

import datetime
from datetime import datetime as dt

#datetime-> str -> file(text)
#file(text) -> str -datetime


parsingFormat = "%Y-%m-%d %H:%M:%S.%f"

'''
%Y%m%d%H%M%S%f
'''

d1 = dt.now() #datetime. datime
d2 = dt.strftime(d1, parsingFormat)#datetime.datetime
#f format
d3 = dt.strptime(d2, parsingFormat) #str -> datetime.datetime
#f format

#print(type(d2), d2)
#print(type(d3), d3)

d4 = datetime.datetime(2030, 10, 2, 18, 0, 2, 200) #datetime
d5 = datetime.datetime(2031, 10, 3, 17, 3, 3, 202)

td = d5 - d4
print(type(td), td) # timedelta

'''print(td.days)
#print(td.hours)
print(td.seconds)
print(td.microseconds)

print(td.total_seconds())'''
d10 = d4 + datetime.timedelta(days=29)
d11 = d4 + datetime.timedelta(days=-29)
print(d10)
print(d11)









