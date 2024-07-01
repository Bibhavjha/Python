# WAP to input 3 different numbers and print the middle number.
a,b,c=input("Enter 3 numbers:").split()
x=int(a)
y=int(b)
z=int(c)
if x>y and x<z or x<y and x>z:
    print(x,"is the middle number")
elif y>x and y<z or y<x and y>z:
    print(y,"is the middle number")
else:
    print(z,"is the middle number")
