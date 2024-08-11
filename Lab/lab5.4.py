# Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square.
class shape:
    def area(self):
        pass
    def perimeter(self):
        pass
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print("Circle area=",3.14*self.radius**2)
    def perimeter(self):
        print("Circle perimeter=", 2*3.14*self.radius)
class square(shape):
    def __init__(self,length):
        self.length=length
    def area(self):
        print("Area of sqaure=",self.length**2)
    def perimeter(self):
        print("perimeter of sqaure=",4*self.length)
class triangle(shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        print("Area of triangle=",(0.5*self.base*self.height))
    def perimeter(self):
        print("perimeter of traingle=",self.base*2+self.height)

c=circle(3)
c.area()
c.perimeter()
s=square(4)
s.area()
s.perimeter()
t=triangle(2,3)
t.area()
t.perimeter()