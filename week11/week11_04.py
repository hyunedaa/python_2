# week11_04.py

class Student:
    def __init__(self):
        self.name = ""
        self.number = ""
        self.dept = ""
        self.birthyear = 0
students = []
for i in range(3):   #type(i) ==> int
    stu = Student()
    stu.name = input("이름 :")
    stu.number = input("학번 :")
    stu.dept = input("학과 : ")
    stu.birthyer = int(input("생년 : "))
    students.append(stu)

for i in students:   #type(i) ==> Student
    print(i.name)

# (1) 동일한 학번이 들어오면 ?
# (2) list가 아닌 dict로 구성해보기.
#     key => number
# (3) while 언제멈출지 ? 어떠하게멈출지?


'''
stu2 = Student()
stu2.name = input("이름 :")
stu2.number = input("학번 :")
stu2.dept = input("학과 : ")
stu2.birthyer = int(input("생년 : "))

stu3 = Student()
stu3.name = input("이름 :")
stu3.number = input("학번 :")
stu3.dept = input("학과 : ")
stu3.birthyer = int(input("생년 : "))
'''
