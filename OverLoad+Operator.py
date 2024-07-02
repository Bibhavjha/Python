# WAP to overload + operator to add two point objects that contains the instance varible x and y
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

# WAP to overload + operator to add two time objects that contains the instance varibales hr,min,sec
class time:
    def __init__(self,hr,mins,sec):
        self.hr=hr
        self.mins=mins
        self.sec=sec
    def __add__(self,other):
        sec=(self.sec+other.sec)
        mins=self.mins+other.mins + sec//60
        hr=self.hr+other.hr+mins//60
        sec=sec%60
        mins=mins%60
        return time(hr,mins,sec)
t1=time(5,40,48)
t2=time(6,50,35)
t3=t1+t2
print("hr=",t3.hr,"mins=",t3.mins,"Sec=",t3.sec)

