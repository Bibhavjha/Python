# Write a python program to add two Distance objects that contain the instance variables km and m
class distnace:
    def __init__(self,km,m):
        self.km=km
        self.m=m
    def __add__(self,other):
        m=self.m+other.m
        km=self.km+other.km + m//1000
        m=m%1000
        return distnace(km,m)
    def __sub__(self,other):
        m=self.m-other.m
        km=self.km-other.km -m//1000
        m=m%1000
        return distnace(km,m)
    
d1=distnace(8,1723)
d2=distnace(11,526)
d3=d1+d2
d4=d1-d2
print(d3.km,d3.m)
print(d4.km,d4.m)