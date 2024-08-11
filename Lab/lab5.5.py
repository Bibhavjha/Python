# Write a python program to add two Point objects.
class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        x=self.x+other.x
        y=self.y+other.y
        return point(x,y)
p1=point(5,20)
p2=point(65,125)
p3=p1+p2
print('x=',p3.x,'y=',p3.y)