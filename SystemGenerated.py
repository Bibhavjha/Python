# WAP to handle ZeroDivisionError
a=int(input("Enter first number"))
b=int(input("Enter second number"))
try:
    c=a//b
    print('Result= ',c)
except ZeroDivisionError as ze:
    print(ze)