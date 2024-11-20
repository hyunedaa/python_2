# week13_04.py
# id:202444079
# name:Kwon Hyun

booklists = []

while True:
    number = input("도서번호:") # 교수님 예시 .strip()
    if number == "": # 교수님 예시 if not number:
        break
    intime = input("대출시간:")
    outtime = input("반납시간:")
    booklist = { 'num':number,
                 'in':intime,
                 'out':outtime}
    booklists.append(booklist)
for booklist in booklists:
    print(booklist['num'], booklist['in'], booklist['out'])
    























