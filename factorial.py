# WAP to input a number and print its factorial only if less than 10
import math
n1=int(input('Enter a number: '))
if n1<10:
    a=math.factorial(n1)
    print("the factorial is",a)
