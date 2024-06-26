# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# class student(person):
#     def __init__(self, name, age,faculty):
#         super().__init__(name, age)
#         self.faculty=faculty
#     def show(self):
#         print(self.name,self.age,self.faculty)
# s=student('ram',20,'bim')
# s.show()


class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(self.name,self.age)
class student(person):
    def __init__(self, name, age,faculty):
        super().__init__(name, age)
        self.faculty=faculty
    
    def show(self):
        super().show()
        print(self.name,self.age,self.faculty)
s=student('ram',20,'bim')
s.show()
