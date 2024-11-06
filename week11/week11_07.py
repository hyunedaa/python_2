# base : week11_03.py
# week11_07.py



class Point:
    def __init__(self, x=0.0 , y= 0.0):
        self.x = x
        self.y = y

p = Point()
p = Point(1,2)
p = Point(x=1)
p = Point(y=1)
print(p.x, p.y)

class Rectangle:
    def __init__(self, x=0.0, y=0.0, w=0.0, h=0.0):
        self.x = x
        self.y = y
        self.width = w
        self.height = h


class Subject:
    def __init__(self,num, nm, t=None, g=None):
        self.number = num
        self.name = nm
        self.teacher = t
        self.grade = g

#Student()
Subject('001', '파이썬')
Subject('001', '파이썬', '이인하')

class Student:
    def __init__(self, num, nm, d , by):
        self.name = nm
        self.number = num
        self.dept = d
        self.birthyear = by



class Rectangle2:
    def __init__(self, sp=Point(), w=0.0, h=0.0):
        self.width = w
        self.height = h
        self.spoint = sp

class Rectangle3:
    def __init__(self, sp=Point(), ep=Point()):
        self.spoint = sp
        self.epoint = ep

r = Rectangle3()
r.spoint.x = 1
r.spoint.y = 1

r.epoint.x = 10
r.epoint.y = 21



        


