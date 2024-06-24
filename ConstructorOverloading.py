from multipledispatch import dispatch
class student:
    @dispatch()
    def __init__(self):
        self.name='ram'
        self.age=20
    @dispatch(str,int)
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(self.name,self.age)
s1=student()
s1.show()
s2=student('hari',21)
s2.show() 