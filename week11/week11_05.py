# week11_05.py
class Test:
    def __init__(self):
        self.name = None
        self.age = None
        
    def func(self, name, age):
        self.name = name
        print(age)

t = Test()
print(t.name)
print(t.age)

t = Test()
t.func("김인하", 20)
print(t.name)
print(t.age)

print("-" * 20)





class In:
    def func(self):
        print("In.func()")

class Out:
    def method(self):
        print("Out.method")

# 안되면 주석.
#method()
#func()

#Out.method()
#In.func()

i = In()
o = Out()


#정식표현 (실제로는 잘 안써)
Out.method(i)
In.func(i)
str.upper("a")
#약식표현 (실제로 쓰는)
o.method()
i.func()
"a".upper()

# 되지만 위험함 OUT 넣어도 가능하고 IN 넣어도 가능함 밑에 처럼 조심해야함
In.func(o)
Out.method(i)

#아예 실행되지 않음.
#o.func()
#i.method()

