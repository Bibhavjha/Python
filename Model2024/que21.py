# Create a class Rectangle containing instance variables
# length and breadth. The class also contains two instance methods area() and
# perimeter() to find area and perimeter of rectangles respectively. Use this class to find
# area and perimeter of two different rectangles.
class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        result=self.length*self.breadth
        print("The area is ",result)
    def perimeter(self):
        result=2*(self.length+self.breadth)
        print("the perimeter is",result)
r1=rectangle(5,6)
r1.area()
r1.perimeter()
r2=rectangle(2.5,1.5)
r2.area()
r2.perimeter()