# week13test_08.py
# id:202444079
# name: kwon hyun

import datetime
from datetime import datetime as dt

f = open("c:/book1/202444079.txt", 'a')

def diff_seconds(intime, outtime):
    if not outtime:
        outtime = dt.now()
    return (outtime - intime).total_seconds()



parsingFormat = "%Y-%m-%d %H:%M:%S"

fullfile = os.path.join(mypath, myfile)

if __main__ == "__name__":
    if not os.path.isdir(mypath):
        os.mkdir(mypath)
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
            if not outtime:
                outtime = None
            else:
                outtime = dt.strptime(outtime, parsingFormat)
            break
            
        booklist = { 'num':number,
                     'in':intime,
                     'out':outtime}
        booklists.append(booklist)
    for booklist in booklists:
        print(booklist['num'], booklist['in'], booklist['out'])
        print(diff_seconds(booklist["in"],booklist["out"]))

    with open(fullfile, 'w') as f:
        
