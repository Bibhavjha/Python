
class person:
    def setP(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(self.name,self.age)
class student(person):
    def setS(self,faculty):
        self.faculty=faculty
    def show(self):
        super().show()
        print(self.faculty)
s1=student()
s1.setP('ram',20)
s1.setS('BIM')
s1.show()