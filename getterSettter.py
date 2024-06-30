# Create a class car with the private instance variables model,price and provide getters
# setters create N car objects, set their details and print only those cars where price is less
# than 2500000
class car:
    @property
    def model(self):
        return self.__model
    @model.setter
    def model(self,model):
        self.__model=model
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self,price):
        self.__price=price
a=int(input("Enter the number of cars"))
cars=[]
for i in range(0,a):
    i=car()
    i.model=input('model of car')
    i.price=float(input('price of car'))
    cars.append(i)
for i in cars:
    if i.price<2500000:
        print(i.model,i.price)


