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
        
c=car()
c.model='nexon'
c.price=57000
print(c.model,c.price)
