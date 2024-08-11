# Write a Python program to create a calculator class. Include methods for basic arithmetic operations.
class calculator:
    def add(self,n1,n2):
        return n1+n2
    def sub(self,n1,n2):
        return n1-n2
    def mul(self,n1,n2):
        return n1*n2
    def div(self,n1,n2):
        return n1/n2
c=calculator()
print("the sum is",c.add(5,6))
print("the diffeence is",c.sub(7,9))
print("the product is",c.mul(6,3))
print("the Divison is",c.div(14,7))
