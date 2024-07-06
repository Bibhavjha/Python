# WAP to input two words and print the longest word.
x,y=input("enter two words:").split()
a=len(x)
b=len(y)
if a>b: 
    print(x," is longest")
else:
    print(y," is longest ")