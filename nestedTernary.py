# using if else as ternary operator WAP to input 3 numbers and print the smallest number
a,b,c=input("Enter three numbers").split()
x=int(a)
y=int(b)
z=int(c)
msg=x if x<y and x<z else y if y<x and y<z else z
print(msg,"is smallest")
