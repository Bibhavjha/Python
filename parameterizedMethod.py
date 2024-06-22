# create a class studnet with the instance variables,names,age,faculty.create a parameterized
# method set() to set student details and a method show () to print student details.create 2 student 
# objects, set the details and print them
class student:
    def set(self,name,age,faculty):
        self.name=name
        self.age=age
        self.faculty=faculty
    def show(self):
        print(self.name,self.age,self.faculty)
s1=student()
s1.set('ram',18,'bim')
s1.show()
s2=student()
s2.set('shyam',19,'bbm')
s2.show()
