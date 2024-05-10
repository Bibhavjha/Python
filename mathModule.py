#WAP to input a number and finds its square root
# import math # imports only the math module not its function
# a=int(input ('enter a number'))
# b=int(math.sqrt(a)) # its always in flaot typecast if required
# print("square root = ",b)


# import math as mt # math is renamed as mt                                      
# a=int(input ('enter a number'))
# b=int(mt.sqrt(a)) # its always in flaot typecast if required
# print("square root = ",b)

from math import * #imports all function of math module
a=int(input ('enter a number'))
b=sqrt(a)
print("square root = ",b)