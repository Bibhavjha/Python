class student:
    def config(self,name,age):
        self.name=name
        self.age=age
    def print(self):
        print(self.name,self.age)
s1=student()
s1.config('ram',20)
s1.print()
s2=student()
s2.config('hari',19)
s2.print()