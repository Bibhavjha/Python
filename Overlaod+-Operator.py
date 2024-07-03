# WAP to overload + and - operators to add and subtract two distance objects that 
# contain variables km and m
# class distnace:
#     def __init__(self,km,m):
#         self.km=km
#         self.m=m
#     def __add__(self,other):
#         m=self.m+other.m
#         km=self.km+other.km + m//1000
#         m=m%1000
#         return distnace(km,m)
#     def __sub__(self,other):
#         m=self.m-other.m
#         km=self.km-other.km -m//1000
#         m=m%1000
#         return distnace(km,m)
# d1=distnace(5,784)
# d2=distnace(2,576)
# d3=d1+d2
# d4=d1-d2
# print(d3.km,d3.m)
# print(d4.km,d4.m)

# 
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
    
a=int(input("Enter kilometer:"))
b=int(input("Enter meter:"))
c=int(input("Enter kilometer for 2nd:"))
d=int(input("Enter meter for 2nd:"))
d1=distnace(a,b)
d2=distnace(c,d)
d3=d1+d2
d4=d1-d2
print(d3.km,d3.m)
print(d4.km,d4.m)
