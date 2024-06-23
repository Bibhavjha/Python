from multipledispatch import dispatch
class student:
    @dispatch(str,int)
    def set(self,name,age):
        self.name=name
        self.age=age
    @dispatch()
    def set(self):
        self.name='hari'
        self.age=20
    def show(Self):
        print(Self.name,Self.age)
s1=student()
s1.set('ram',20)
s1.show()
s2=student()
s2.set('ram',20)
s2.show()