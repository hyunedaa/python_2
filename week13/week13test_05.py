# week13test_05.py
# id:202444079
# name: kwon hyun

import datetime
from datetime import datetime as dt

parsingFormat = "%Y-%m-%d %H:%M:%S"

booklists = []

while True:
    number = input("도서번호:")
    if number == "":
        break
    while True:
        try:
            intime = input("대출시간:").strip()
            if intime:
                intime = dt.strptime(intime, parsingFormat)
                break
        except:
            pass
        
    while True:
        outtime = input("반납시간:").strip()
        if outtime == "":
            None
        else:
            outtime = dt.strptime(outtime, parsingFormat)
        break
    
    booklist = { 'num':number,
                 'in':intime,
                 'out':outtime}
    booklists.append(booklist)
for booklist in booklists:
    print(booklist['num'], booklist['in'], booklist['out'])
