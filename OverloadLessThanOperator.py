class person:
    def __init__(self,name,age):
       self.name=name
       self.age=age
    def __lt__(self,other):
      return self.age<other.age

p1=person('ram',25)
p2=person('hari',21)
if p1<p2:
    print(p1.name,p1.age)
else:
    print(p2.name,p2.age)

