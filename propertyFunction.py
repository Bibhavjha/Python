class car:
        def set_model(self,model):
           self.__model=model
        def get_model(self):
            return self.__model
        def set_price(self,price):
            self.__price=price
        def get_price(self):
            return self.__price
        Model=property(get_model,set_model) # Model is property name 
        Price=property(get_price,set_price) #price is property name010j
c=car()
c.Model='nexon'
c.Price=57000
print(c.Model,c.Price)
