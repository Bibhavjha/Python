from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class circle(shape):
    def __init__(self,radius):
       self.radius=radius
    def area(self):
        return 3.14*self.radius**2
c=circle(3.8)
print("Area is",c.area())