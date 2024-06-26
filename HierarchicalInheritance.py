class father:
    def fun1(self):
        print("inside father class")
class son(father):
    def fun2(self):
        print("inside son class")
class daughter(father):
    def fun3(self):
        print("inside daughter class")
s=son()
s.fun2()
s.fun1()
d=daughter()
d.fun1()
d.fun3()