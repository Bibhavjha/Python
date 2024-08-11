#  Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
class circle:
    def __init__(self,radius):
      self.radius=radius
    def area(self):
       return 3.14*self.radius**2
    def perimeter(self):
       return 2*3.14*self.radius
c=circle(5)
print("Area=",c.area(),"perimeter=",c.perimeter())
    