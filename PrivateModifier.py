class student:
    def set(self,name,age):
        self.__name=name
        self.__age=age
    def show(self):
        print(self.__name,self.__age)
s=student()
s.set('ram',19) #set is public and can be acessed here 
s.show() #show is public and can be accessed anywhere
#print(s.__name,s.__age) error #name and age are private and can't be accessed here