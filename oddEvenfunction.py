# WAP to take a number,pass it to a function that checks odd/evenv 
def check(a):
    if a%2==0:
        print(a, "is even")
    else:
        print(a,"is odd")
x=int(input("enter a number"))
check(x)
    