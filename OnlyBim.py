# create a class studnet with the instance variables,names,age,faculty.create a parameterized
# method set() to set student details and a method show () to print student details.create 5 student 
# objects, and print only those records who study BIM
class student:
    def set(self,name,age,faculty):
        self.name=name
        self.age=age
        self.faculty=faculty
    def show(self):
        print(self.name,self.age,self.faculty)
s1=student()
s1.set('ram',18,'bim')

s2=student()
s2.set('shyam',19,'bbm')

s3=student()
s3.set('gita',19,'bim')

s4=student()
s4.set('hari',19,'bbm')

s5=student()
s5.set('krishna',19,'bca')

students=[s1,s2,s3,s4,s5]
for student in students:
    if student.faculty=='bim':
        student.show()