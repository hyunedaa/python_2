# week13test_04.py
# id:202444079
# name:Kwon Hyun


import datetime
from datetime import datetime as dt

parsingFormat = "%Y-%m-%d %H:%M:%S.%f"

booklists = []

while True:
    number = input("도서번호:")
    if number == "":
        break
    intime = input("대출시간:")
    intime = dt.strptime(intime, parsingFormat)
    outtime = input("반납시간:")
    outtime = dt.strptime(outtime, parsingFormat)
    booklist = { 'num':number,
                 'in':intime,
                 'out':outtime}
    booklists.append(booklist)
for booklist in booklists:
    print(booklist['num'], booklist['in'], booklist['out'])






    
