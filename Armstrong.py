a=int(input("Enter a number"))
n=a
rev=0
while n>0:
    r=n%10
    rev=rev+r**3
    n=n//10
if a==rev:
    print("it is Armstrong")
else:
    print("not Armstrong")