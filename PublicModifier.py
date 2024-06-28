class student:
    def set(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(self.name,self.age)
s=student()
s.set('ram',19) #set is public and can be acessed here 
s.show() #show is public and can be accessed anywhere
print(s.name,s.age) #name and age are public can be accessed here