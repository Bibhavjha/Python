class student:
    def set(self,name,age,faculty):
        self.__name=name #name is private
        self._age=age #age is protected 
        self.faculty=faculty #faculty is public
class parttimeStudent(student):
    def show(self):
        # print(self.__name) #error 
        print(self._age)
        print(self.faculty)
s=parttimeStudent()
s.set('ram',20,'bim')
s.show()
