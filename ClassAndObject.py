# first class and object program
class student:
    def config(self): #we can write anything other than self but is usual
        # config()-instance method or method
        self.name='ram'
        self.age=17  #name and age are instance variables or attributes
s1=student() #s1 is the object
s1.config()
print(s1.name,s1.age)

class student:
    def config(self): #we can write anything other than self but is usual
        # config()-instance method or method
        self.name='ram'
        self.age=17  #name and age are instance variables or attributes
    def print(self):
        print(self.name,self.age)
s1=student()
s1.config()
s1.print()
